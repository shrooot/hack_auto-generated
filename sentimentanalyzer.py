from transformers import AutoModelForSequenceClassification, AutoTokenizer
from scipy.special import softmax
import numpy as np
import csv
import urllib.request

class SentimentAnalyzer:
    def __init__(self, task='sentiment'):
        self.model_name = f"cardiffnlp/twitter-roberta-base-{task}"
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.labels = self._load_labels()

    def _load_labels(self):
        mapping_link = f"https://raw.githubusercontent.com/cardiffnlp/tweeteval/main/datasets/sentiment/mapping.txt"
        with urllib.request.urlopen(mapping_link) as f:
            html = f.read().decode('utf-8').split("\n")
            csvreader = csv.reader(html, delimiter='\t')
            labels = [row[1] for row in csvreader if len(row) > 1]
        return labels

    def preprocess(self, text):
        new_text = []
        for t in text.split(" "):
            t = '@user' if t.startswith('@') and len(t) > 1 else t
            t = 'http' if t.startswith('http') else t
            new_text.append(t)
        return " ".join(new_text)

    def analyze_sentiment(self, text):
        text = self.preprocess(text)
        encoded_input = self.tokenizer(text, return_tensors='pt')
        model = AutoModelForSequenceClassification.from_pretrained(self.model_name)
        output = model(**encoded_input)
        scores = output.logits.detach().numpy()
        scores = softmax(scores)
        
        ranking = np.argsort(scores)
        ranking = ranking[::-1]
        
        results = []
        for i in range(scores.shape[1]):
            label = self.labels[ranking[0, i]]
            score = scores[0, ranking[0, i]]
            results.append({"label": label, "score": np.round(float(score), 4)})
        
        return results

if __name__ == "__main__":
    # Example usage
    analyzer = SentimentAnalyzer()
    text = "I am facing some issues with the app please help, i am under the water😊"
    results = analyzer.analyze_sentiment(text)
    
    print(f"Sentiment Analysis for: '{text}'")
    for i, result in enumerate(results):
        print(f"{i+1}) {result['label']} {result['score']}")
