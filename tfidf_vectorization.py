    #importing libraries
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

    #loading train dataset
df = pd.read_csv("processed_train.csv")

    #initialize tf-idf
vectorizer = TfidfVectorizer()

    #leaning and converting words(unique,common)  into numbers(weight)
X_train = vectorizer.fit_transform(df["cleaned_text"])

    # printing the shape of the output  (x-shape-> stores the resulting grid of numbers)
# print("Shape:", X_train.shape)
# print("Vocabulary size:", len(vectorizer.vocabulary_))
# print("First document vector:", X_train[0].toarray())

    # loading testing dataset
test_df=pd.read_csv("test_processing.csv")   
 
    #changing the text into number without learning
X_test=vectorizer.transform(test_df["cleaned_text"])
# print("Testing shape:",X_test.shape)

y_train = df["label"]
y_test = test_df["label"]

# print("Training labels:", y_train.shape)
# print("Testing labels:", y_test.shape)

# print("\nTraining category distribution:")
# print(y_train.value_counts().sort_index())