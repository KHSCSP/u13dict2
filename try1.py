# ---------- part 1, a mixed list -------------
print("\n\n----a list with mixed types and bad data----")
data = ['8', '3', '4', '5', '2', ",", '4', '0', '3', '8', '2', '1', '-3', '-5', '-1', ".", 6, 6, 4, 1, -5, 9, 8, 
6, 7, "bologna", 5, 0, 4, 8, 9, 9, "\n", 6, '0', 9, 1]
# our list is supposed to only contain integers
# create a list of only the integer items
# this will require you to loop through, 'try' to convert to integer, and append to a list
# TODO
lst = []

  
print("\nshould be good integers:", lst)



# the sensor malfunctioned! 
# the list should only have positive integers
# how many times did the sensor malfunction?
# TODO
count = 0

    
print("\nthis many malfunctions:", count)


# make a new list of only the positive numbers
# TODO
lst2 = []


print("\nhere's the good stuff:", lst2)



print("\n\n---- analyzing a list of integers ----")
# now that we have valid data:
# find the sum and average
# count how many items are less than 5
# TODO



print("\nthere are this many:")


# we need to count how many times each digit appears
# make a dictionary where each key-value pair is i: count(i)
counts = {}

print("\nhere's the counts:", counts)

# what is the max count?
print("here's the max number of times:")



# ---------- part 2, a list of words -------------
print("\n--- last part, the constitution ---")
# --- load the data ---
s = ''
f = open('u13dict2/constitution.txt', "r")
s = f.read()
f.close()

# become familiar with the data
print("\nlength of string:")
print("a sample from the string:")

# clean up the data
unwanted = ["\n", ".", "!", ",", "?", ":"]

print("\na sample after cleaning:")

# convert to a list of words


# create a list of unique words


# make a list of words that occur only once
only_once = []

print("\nhere are the words that occur only once:", only_once)




# create a dictionary
# key=word: value=count of that word




# what is the most common word?

