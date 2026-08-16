from transformers import pipeline

classifier = pipeline(
    "sentiment-analysis",
    model="distilbert-base-uncased-finetuned-sst-2-english"
)


def analyze_sentiment(text):

    if text.strip() == "":
        return "Neutral"

    result = classifier(text)[0]

    if result["label"] == "POSITIVE":
        return "Positive"
    else:
        return "Negative"