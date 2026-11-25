from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

from tfidf_vectorization import X_test,X_train,y_test,y_train
from sklearn.metrics import classification_report,confusion_matrix


model=LogisticRegression(max_iter=1000)
print("Model training completed!")
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
print(y_pred[:10])

accuracy=accuracy_score(y_test,y_pred)
print("Logistic Regression accuracy",accuracy)
print("Accuracy percentage",accuracy*100)


category_names=["World","Sports","Business","Sci/Tech"]
print("\nclassification_Report")
print(classification_report(
    y_test,
    y_pred,
    target_names=category_names
))
print("\nconfusion_matrix")
print(confusion_matrix(y_test,y_pred))