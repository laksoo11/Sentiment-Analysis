import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import GetOldTweets3 as got

# Load the trained model and vectorizer
model = joblib.load('c:/Users/ankit/Desktop/LORU/sentiment-analysis-app/streamlit_app/models/trained_model.pkl')
vectorizer = joblib.load('c:/Users/ankit/Desktop/LORU/sentiment-analysis-app/streamlit_app/models/vectorizer.pkl')

# Function to predict sentiment
def predict_sentiment(text):
    text_vectorized = vectorizer.transform([text])  # No need to convert to dense array
    sentiment = model.predict(text_vectorized)[0]  # Predict sentiment
    return sentiment

# Function to map sentiment to label
def get_sentiment_label(sentiment):
    if sentiment == 1:
        return "Positive"
    elif sentiment == -1:
        return "Negative"
    else:
        return "Neutral"

# Streamlit app layout
st.title("Sentiment Analysis Web Application")
st.write("Enter the text you want to analyze:")

# Text input for user
user_input = st.text_area("Text Input")

if st.button("Analyze"):
    if user_input:
        sentiment = predict_sentiment(user_input)
        sentiment_label = get_sentiment_label(sentiment)
        st.write(f"Predicted Sentiment: {sentiment_label}")
    else:
        st.write("Please enter some text to analyze.")

# Trend visualization
st.write("## Trend Visualization")

# Example data for visualization
data = {
    'Hashtag': ['#AI', '#ML', '#DataScience', '#BigData', '#DeepLearning'],
    'Count': [100, 150, 200, 250, 300]
}
df = pd.DataFrame(data)

# Plot using matplotlib
fig, ax = plt.subplots()
ax.bar(df['Hashtag'], df['Count'])
ax.set_xlabel('Hashtag')
ax.set_ylabel('Count')
ax.set_title('Hashtag Trend')
st.pyplot(fig)

# Plot using plotly
fig = px.bar(df, x='Hashtag', y='Count', title='Hashtag Trend')
st.plotly_chart(fig)

# Live social media tracking via GetOldTweets3
st.write("## Live Social Media Tracking")

# Function to fetch tweets using GetOldTweets3
def fetch_tweets(keyword, limit=100):
    tweetCriteria = got.manager.TweetCriteria().setQuerySearch(keyword).setMaxTweets(limit)
    tweets = got.manager.TweetManager.getTweets(tweetCriteria)
    return [tweet.text for tweet in tweets]

# Input for live tracking
keyword = st.text_input("Enter a keyword for live tracking:")
if st.button("Track"):
    if keyword:
        tweets = fetch_tweets(keyword)
        st.write(f"Fetched {len(tweets)} tweets for keyword: {keyword}")
        for tweet in tweets:
            st.write(tweet)
    else:
        st.write("Please enter a keyword to track.")

# Run the app using the command below:
# python -m streamlit run c:/Users/ankit/Desktop/LORU/sentiment-analysis-app/notebooks/app.py