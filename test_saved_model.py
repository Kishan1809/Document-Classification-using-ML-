import joblib
model=joblib.load("svm_model.pkl")
vectorizer=joblib.load("tfidf_vectorizer.pkl")


# Sample news
from preprocessing import preprocess_text

news = "Stock market prices rise after major economic reforms"

cleaned_news = preprocess_text(news)

news_vector = vectorizer.transform([cleaned_news])

prediction = model.predict(news_vector)

category_mapping = {
    0: "World",
    1: "Sports",
    2: "Business",
    3: "Sci/Tech"
}

predicted_category = category_mapping[prediction[0]]

print("News:", news)
print("Predicted category:", predicted_category)


