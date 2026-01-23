from transformers import pipeline

class TopicClassifier:
    def __init__(self):
        self.classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
        self.labels=["Politics", "Sports", "Technology", "Science", "Society", "Health", "Entertainment", "Business"]

    def classify(self, text):
        return self.classifier(text, self.labels)