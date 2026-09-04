"""
ML-01 — What Is Machine Learning?
A simple demonstration showing traditional vs. machine learning concepts.
"""

def traditional_spam_filter(message):
    spam_words = ["win", "free", "prize", "urgent"]
    return "spam" if any(w in message.lower() for w in spam_words) else "not spam"

class SimpleSpamModel:
    def __init__(self):
        self.threshold = None

    def train(self, examples):
        spam_vals = [val for val, label in examples if label == "spam"]
        safe_vals = [val for val, label in examples if label == "not spam"]
        self.threshold = (sum(spam_vals) / len(spam_vals) + sum(safe_vals) / len(safe_vals)) / 2

    def predict(self, val):
        return "spam" if val >= self.threshold else "not spam"

if __name__ == "__main__":
    print("Running ML-01 Demo...")
    print("Traditional Rule Filter:", traditional_spam_filter("Win a free prize!"))
    
    model = SimpleSpamModel()
    model.train([(9, "spam"), (1, "not spam")])
    print("Learned Threshold:", model.threshold)
    print("Prediction for value 7:", model.predict(7))
