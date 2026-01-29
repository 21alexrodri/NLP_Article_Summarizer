from transformers import pipeline

class ArticleSummarizer:
    def __init__(self, model_name="sshleifer/distilbart-cnn-12-6"):
        self.summarizer = pipeline("summarization", model=model_name)

    def summarize(self, text, max_length=120, min_length=40):
        # quedarse solo con los primeros caracteres
        text = text[:3000]

        summary = self.summarizer(
            text,
            max_length=max_length,
            min_length=min_length,
            do_sample=False
        )

        return summary[0]["summary_text"]
