from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from labels.labels import Label

class TopicClassifier2:
    # CLASSIFICA EN VECTORS
    def __init__(self):
        self.classifier = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")
        self.labels = Label.values()
        self.label_embeddings = self.classifier.encode(
            self.labels,
            convert_to_tensor=True
        )

    '''
        text: str - text a classificar
    '''
    def classify(self, text):
        text_embedding = self.classifier.encode(
            text,
            convert_to_tensor=True
        )

        scores = cosine_similarity(
            [text_embedding.cpu().numpy()],
            self.label_embeddings.cpu().numpy()
        )[0]

        ranked = sorted(
            zip(self.labels, scores),
            key=lambda x: x[1],
            reverse=True
        )

        return ranked