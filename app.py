from pdf_extraction import extract_pdf_text
import streamlit as st
import joblib
from preprocessing import preprocess_text

model = joblib.load("svm_model.pkl")
vectorizer = joblib.load("tfidf_vectorizer.pkl")

st.title("Intelligent Document Classification System")

st.write(
    "Classify news articles into World, Sports, Business and Sci/Tech categories."
)

uploaded_pdf = st.file_uploader(
    "Or upload a PDF document",
    type=["pdf"]
)

uploaded_file = st.file_uploader(
    "Or upload a TXT document",
    type=["txt"]
)

if uploaded_pdf is not None:
    pdf_text = extract_pdf_text(uploaded_pdf)
    st.text_area("Extracted PDF content", pdf_text, height=150)

if uploaded_file is not None:
    # file_text = uploaded_file.getvalue().decode("utf-8")
    try:
        file_text = uploaded_file.getvalue().decode("utf-8")
    except UnicodeDecodeError:
        st.error("Unable to read this file. Please upload a UTF-8 encoded TXT file.")
        file_text = ""
    st.text_area("Uploaded document content", file_text, height=150)


manual_news = st.text_area("Enter your news article")

if uploaded_file is not None:
    news = file_text
else:
    news = manual_news

if uploaded_pdf is not None:
    news = pdf_text
else:
    news = manual_news

if st.button("Classify news"):

    if news.strip() == "":
        st.warning("Please enter some news text.")

    else:
        cleaned_news = preprocess_text(news)

# Extract words
        tokens = cleaned_news.split()

        # Keep alphabetic words
        alphabetic_words = [word for word in tokens if word.isalpha()]

        # Check how many words exist in the trained vocabulary
        known_words = [
            word for word in alphabetic_words
            if word in vectorizer.vocabulary_
        ]

        if len(alphabetic_words) < 3:
            st.warning("Please enter a meaningful news article.")

        elif len(known_words) < 3:
            st.warning("Your input contains too few recognizable words. Please enter a proper news article.")

        else:
            news_vector = vectorizer.transform([cleaned_news])
            prediction = model.predict(news_vector)

            category_mapping = {
                0: "World",
                1: "Sports",
                2: "Business",
                3: "Sci/Tech"
            }

            predicted_category = category_mapping[prediction[0]]
            st.success(f"Predicted Category: {predicted_category}")