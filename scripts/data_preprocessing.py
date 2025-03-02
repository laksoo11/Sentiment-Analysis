import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from sklearn.model_selection import train_test_split

nltk.download('stopwords')

def clean_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)  # Remove URLs
    text = re.sub(r'\@\w+|\#', '', text)  # Remove mentions and hashtags
    text = re.sub(r'\d+', '', text)  # Remove numbers
    text = re.sub(r'[^\w\s]', '', text)  # Remove punctuation
    return text

def preprocess_data(file_path):
    # Load raw data
    data = pd.read_csv(file_path)
    
    # Clean text data
    data['cleaned_text'] = data['text'].apply(clean_text)
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    data['cleaned_text'] = data['cleaned_text'].apply(lambda x: ' '.join([word for word in x.split() if word not in stop_words]))
    
    # Split data into features and labels
    X = data['cleaned_text']
    y = data['label']
    
    # Split into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Save processed data
    processed_data = pd.DataFrame({'text': X_test, 'label': y_test})
    processed_data.to_csv('data/processed/processed_data.csv', index=False)
    
    return X_train, X_test, y_train, y_test