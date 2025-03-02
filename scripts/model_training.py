import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib
import os

# Load the preprocessed data
data_path = os.path.join('data', 'processed', 'processed_data.csv')
data = pd.read_csv(data_path)

# Define features and target variable
X = data['text']  # Assuming 'text' is the column with the text data
y = data['label']  # Assuming 'label' is the column with the sentiment labels

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorization (you can use CountVectorizer or TfidfVectorizer)
from sklearn.feature_extraction.text import TfidfVectorizer

vectorizer = TfidfVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train_vectorized, y_train)

# Evaluate the model
y_pred = model.predict(X_test_vectorized)
print(classification_report(y_test, y_pred))

# Save the trained model and vectorizer
joblib.dump(model, os.path.join('models', 'trained_model.pkl'))
joblib.dump(vectorizer, os.path.join('models', 'vectorizer.pkl'))