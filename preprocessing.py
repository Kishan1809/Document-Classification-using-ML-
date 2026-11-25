
import string
def preprocess_text(text):
    
    # Step 1: lowercase
    lower_case = text.lower()
    # Step 2: remove punctuation
    table = str.maketrans("", "", string.punctuation)
    removed_punctuation = lower_case.translate(table)

    # Step 3 and 4: normalize whitespace and tokenize
    tokens = removed_punctuation.split()

    # Step 5: return cleaned text
    clean_text = " ".join(tokens)

    return clean_text


text = "THE Stock Market is RISING!!! ,  ,,Prices are Increasing."

# print(preprocess_text(text))
