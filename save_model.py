import joblib
from tfidf_vectorization import vectorizer
from linear_svm import model

joblib.dump(model,"svm_model.pkl")
joblib.dump(vectorizer,"tfidf_vectorizer.pkl")
print("Model and vectorizer saved successfully!")