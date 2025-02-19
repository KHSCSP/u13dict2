# ---------- part 2, a list of words -------------
print("\n--- last part, the constitution ---")
# --- load the data ---
s = ''
f = open('constitution.txt', "r")
s = f.read()
f.close()

# become familiar with the data
print("\nlength of string:")
print("a sample from the string:")


# clean up the data
unwanted = ["\n", ".", "!", ",", "?", ":"]

print("\na sample after cleaning:")



# convert to a list of words
words = []
print("\na sample of the list:")
print("length of words:")




# make a list of words that occur only once
only_once = []

print("\nhere are the words that occur only once:", only_once)




# create a list of unique words
unique_words = []

print("\na sample of unique:", unique_words[:10])
print("length of unique words:", len(unique_words))




# create a dictionary
# key=word: value=count of that word
counts = {}


print("here's the counts:", counts)



# what is the most common word?
max_count = 0
max_word = ''

print("\n", max_word, "is the most common")
print(max_count, "times")

