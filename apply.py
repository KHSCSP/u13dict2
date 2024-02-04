f = open("pi_digits.txt", "r")  # open the file for reading
pi = f.read() # read the data into one long string
f.close() # close the file to release memory

print("\n--- part 1, working with a string ---")

# remove any unwanted characters (spaces, newlines, decimals)
# it should look like this when finished: 3141592653589793238462643383279


# how many digits do we have? (what is the length of the variable?)



# how many zeros? (use the count function)



# once your program is working, change the file at the top to "pi_million_digits.txt" and run your code again
# YOU MAY NEED TO COMMENT OUT SOME PREVIOUS PRINT STATEMENTS





#---------------------------------------------------
print("\n\n---- part 2, working with a list of integers ---")
# ---SWITCH BACK TO THE "SHORT" VERSION OF PI---
# convert your string into a list of integers
# your variable should look like this:
# [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2, 6, 4, 3, 3, 8, 3, 2, 7, 9]
# hint: create a new list using list comprehension to iterate through 'pi'




# how many zeros? (use the count function)




# count how many digits are less than 5 (this will require a loop)




# we need to count how many times each digit appears
# make a dictionary where each key-value is digit: count(digit)




# once your program is working, change the file to "pi_million_digits.txt" and run your code again


# when that is working, uncomment the following lines and run your program
# import matplotlib
# import matplotlib.pyplot as plt
# import numpy as np
# x = np.array(list(counts.keys()))
# y = np.array(list(counts.values()))
# plt.bar(x,y)
# plt.show()



# before moving forward you'll need to comment out the bar plot




#---------------------------------------------------
print("\n\n---- part 3, working with a list of words ---")
# uncomment these lines when ready
# f = open('declaration.txt', "r")
# s = f.read()
# f.close()

# become familiar with the data
# how many characters? (length of string)
# display a sample



# clean up the data
# lowercase
# remove newlines, punctuation



# display a sample of the cleaned up string




# convert to a list of words (use the split function)
# how many words? (length of your list)




# how many times does the word 'state' appear? (use the count function)



# choose another word of your own, count that word




# create a list of unique words (use the set function)



# create a dictionary
# each key-value should be word: count word




# what word occurs most frequently?








# optional challenge
# create a plot of words and the number of times those words appear
# this will require a pygame trinket




# optional challenge
# go back and remove the most common word
# repeat this until the most commn word is non-trivial
