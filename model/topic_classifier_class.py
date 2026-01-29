from transformers import pipeline
from labels.labels import Label

class TopicClassifier:
    # CLASSIFICA EN PORCENTATGE
    def __init__(self):
        self.classifier = pipeline("zero-shot-classification", model="facebook/bart-large-mnli")
        self.labels = Label.values()

    def classify(self, text):
        return self.classifier(text, self.labels)