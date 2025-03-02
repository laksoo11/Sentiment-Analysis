with open("path/to/sentiment_model.pkl", "rb") as f:
    model = pickle.load(f)

{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9538db6d-37ed-4729-ba33-40d6832fff96",
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: 'sentiment_model.pkl'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[1], line 5\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mpickle\u001b[39;00m\n\u001b[0;32m      4\u001b[0m \u001b[38;5;66;03m# Load trained model\u001b[39;00m\n\u001b[1;32m----> 5\u001b[0m \u001b[38;5;28;01mwith\u001b[39;00m \u001b[38;5;28mopen\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124msentiment_model.pkl\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mrb\u001b[39m\u001b[38;5;124m\"\u001b[39m) \u001b[38;5;28;01mas\u001b[39;00m f:\n\u001b[0;32m      6\u001b[0m     model \u001b[38;5;241m=\u001b[39m pickle\u001b[38;5;241m.\u001b[39mload(f)\n\u001b[0;32m      8\u001b[0m \u001b[38;5;66;03m# Streamlit UI\u001b[39;00m\n",
      "File \u001b[1;32m~\\anaconda3\\Lib\\site-packages\\IPython\\core\\interactiveshell.py:324\u001b[0m, in \u001b[0;36m_modified_open\u001b[1;34m(file, *args, **kwargs)\u001b[0m\n\u001b[0;32m    317\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m file \u001b[38;5;129;01min\u001b[39;00m {\u001b[38;5;241m0\u001b[39m, \u001b[38;5;241m1\u001b[39m, \u001b[38;5;241m2\u001b[39m}:\n\u001b[0;32m    318\u001b[0m     \u001b[38;5;28;01mraise\u001b[39;00m \u001b[38;5;167;01mValueError\u001b[39;00m(\n\u001b[0;32m    319\u001b[0m         \u001b[38;5;124mf\u001b[39m\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mIPython won\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mt let you open fd=\u001b[39m\u001b[38;5;132;01m{\u001b[39;00mfile\u001b[38;5;132;01m}\u001b[39;00m\u001b[38;5;124m by default \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    320\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mas it is likely to crash IPython. If you know what you are doing, \u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    321\u001b[0m         \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124myou can use builtins\u001b[39m\u001b[38;5;124m'\u001b[39m\u001b[38;5;124m open.\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m    322\u001b[0m     )\n\u001b[1;32m--> 324\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m io_open(file, \u001b[38;5;241m*\u001b[39margs, \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mkwargs)\n",
      "\u001b[1;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: 'sentiment_model.pkl'"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pickle\n",
    "\n",
    "# Load trained model\n",
    "with open(\"sentiment_model.pkl\", \"rb\") as f:\n",
    "    model = pickle.load(f)\n",
    "\n",
    "# Streamlit UI\n",
    "st.title(\"Sentiment Analysis App\")\n",
    "st.write(\"Enter text to analyze its sentiment.\")\n",
    "\n",
    "# User Input\n",
    "user_input = st.text_area(\"Enter your text here:\")\n",
    "\n",
    "if st.button(\"Analyze Sentiment\"):\n",
    "    if user_input:\n",
    "        prediction = model.predict([user_input])  # Modify if using vectorization\n",
    "        sentiment = \"Positive 😊\" if prediction == 1 else \"Negative 😢\"\n",
    "        st.write(f\"**Predicted Sentiment:** {sentiment}\")\n",
    "    else:\n",
    "        st.warning(\"Please enter some text.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e2b233f4-3ec1-420b-89e1-dbd7b241e4bb",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
