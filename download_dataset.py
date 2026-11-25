from datasets import load_dataset

dataset = load_dataset("fancyzhx/ag_news")

dataset["train"].to_csv("train.csv")
dataset["test"].to_csv("test.csv")

print("Dataset downloaded successfully!")
print(dataset)