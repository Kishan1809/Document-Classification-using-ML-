import pandas as pd
from preprocessing import preprocess_text

df=pd.read_csv("test.csv")
df["cleaned_text"]=df["text"].apply(preprocess_text)
print(df[["cleaned_text","text"]].head())
print("Cleaned text count:", df["cleaned_text"].count())

print(df["cleaned_text"].isnull().sum())
df.to_csv("test_processing.csv", index=False)
