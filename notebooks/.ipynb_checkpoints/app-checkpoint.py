import streamlit as st
import pandas as pd
import joblib

# Load the trained model and vectorizer
model = joblib.load('models/trained_model.pkl')
vectorizer = joblib.load('models/vectorizer.pkl')  # Load the vectorizer

# Function to predict sentiment
def predict_sentiment(text):
    text_vectorized = vectorizer.transform([text]).toarray()  # Convert to dense 2D array
    sentiment = model.predict(text_vectorized)[0]  # Predict sentiment
    return sentiment

# Streamlit app layout
st.title("Sentiment Analysis Web Application")
st.write("Enter the text you want to analyze:")

# Text input for user
user_input = st.text_area("Text Input")

if st.button("Analyze"):
    if user_input:
        sentiment = predict_sentiment(user_input)
        st.write(f"Predicted Sentiment: {sentiment}")
    else:
        st.write("Please enter some text to analyze.")
