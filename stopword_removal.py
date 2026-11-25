from text_processing import clean_text

tokens = clean_text.split()

stop_words = {"the", "is", "are", "a", "an", "in", "of", "and"}

filtered_tokens = []

for i in tokens:
    if i not in stop_words:
       filtered_tokens.append(i)
print(filtered_tokens)