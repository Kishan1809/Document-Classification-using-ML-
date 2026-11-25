from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

from sklearn.metrics import classification_report,confusion_matrix

# import LinearSVC from sklearn.svm.
from tfidf_vectorization import X_test,X_train,y_test,y_train
# Reuse your existing TF-IDF training and testing data.
model=LinearSVC()
# Create the model.

model.fit(X_train,y_train)
print("Model Traininh completed!")
# Train it using .fit().

y_pred=model.predict(X_test)
# Predict on X_test.

accuracy=accuracy_score(y_test,y_pred)
print("Accuracy of SVM:",accuracy)
print("Accuracy percentage",accuracy*100)
# Calculate accuracy using accuracy_score.
category_names=["World","Sports","Business","Sci/Tech"]
print("\nClassification report")
print(classification_report(
       y_test,
       y_pred,
       target_names=category_names
))
print("\nConfusion matrix")
print(confusion_matrix(y_test,y_pred))
# Generate the classification report.