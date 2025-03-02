import pickle
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

def load_model(model_path):
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model

def load_vectorizer(vectorizer_path):
    with open(vectorizer_path, 'rb') as file:
        vectorizer = pickle.load(file)
    return vectorizer

def predict_sentiment(text, model, vectorizer):
    text_vectorized = vectorizer.transform([text])
    prediction = model.predict(text_vectorized)
    return prediction[0]

if __name__ == "__main__":
    model_path = '../models/trained_model.pkl'
    vectorizer_path = '../models/tfidf_vectorizer.pkl'  # Assuming you save the vectorizer as well

    model = load_model(model_path)
    vectorizer = load_vectorizer(vectorizer_path)

    sample_text = "I love using this application!"
    sentiment = predict_sentiment(sample_text, model, vectorizer)
    print(f"The sentiment of the text is: {sentiment}")