from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from tfidf_vectorization import X_train,y_train,X_test,y_test

from sklearn.metrics import classification_report,confusion_matrix

#initialize model
model=MultinomialNB()
#Model training 
model.fit(X_train,y_train)
print("Model Training completed!")

# Make prediction
y_pred=model.predict(X_test)
print(y_pred[:10])

# accuracy_prediction
accuracy=accuracy_score(y_test,y_pred)
print("Naive bayes accuracy",accuracy)
print("Accuracy percentage",accuracy*100)

# confusion matrix
category_names = ["World", "Sports", "Business", "Sci/Tech"]

print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    target_names=category_names
))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))