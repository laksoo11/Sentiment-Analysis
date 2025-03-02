{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "9538db6d-37ed-4729-ba33-40d6832fff96",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-02-28 15:00:49.180 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\Dell\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2025-02-28 15:00:49.183 Session state does not function when running a script without `streamlit run`\n"
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
