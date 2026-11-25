import string

text = "THE Stock Market is RISING!!! ,  ,,Prices are Increasing."

lower_case = text.lower()  # converting into lowercase

table = str.maketrans("", "", string.punctuation) # creating a rule book or table and marking punctuation as None(which is to be deleted)
clean_text = lower_case.translate(table) # it deletes the marked punctuation and leaves the space

clean_text = " ".join(clean_text.split()) # .split() splits all words and " ".join joins all words together

# print(clean_text)