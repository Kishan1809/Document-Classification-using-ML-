import pandas as pd
df=pd.read_csv("train.csv")
print(df.isnull().sum())
print(df.duplicated().sum())
print(df.nunique())
# print(df["label"].value_counts().sort_index())


category_mapping = {
    0: "World",
    1: "Sports",
    2: "Business",
    3: "Sci/Tech"
}
df["category"] = df["label"].map(category_mapping)
print(df["category"].value_counts())