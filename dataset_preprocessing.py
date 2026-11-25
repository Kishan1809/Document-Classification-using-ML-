import pandas as pd
from preprocessing import preprocess_text

df=pd.read_csv("train.csv")

df["cleaned_text"]=df["text"].apply(preprocess_text)
print(df[["text", "cleaned_text"]].head())

print("Cleaned text count:", df["cleaned_text"].count())

print(df["cleaned_text"].isnull().sum())
df.to_csv("processed_train.csv", index=False)

print(df.shape)