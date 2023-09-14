#############################complete slide 1 challenge from week 4 slideshow##########
#############################20 minutes################################################

##########################Reviewing somethings

# indexing strings -- slide 4
my_text = 'this is a text'
result = my_text  #get the index of the letter a
print(result)
print(my_text.find("a"))

#get the index of the third letter from the end of the text
print(my_text.find("e"))

# find the index of the letter s
print(my_text.find("s"))
###slide 5
# string[start:stop:step]
#example
# text = "Hello, World!"
# print(text[7:12])  # prints "World"
text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# Get the substring CDE and put in a variable
print(text[2:5])
#substring1= 
#get the first letter all the way to the 4th letter
print(text[:4])
#get the first letter to the final letter and skip every 3rd letter
print(text[0::3])
# Built-in methods:
# Python has a variety of built-in methods to work with substrings.

# a. str.find():
# This method returns the lowest index of the substring if found in the given string. If it's not found, it returns -1.
# text = "Hello, World!"
# print(text.find("World"))  # prints 7
# print(text.find("Earth"))  # prints -1

#################################Extracting Sub-Strings###################################
# Extracting Sub-Strings Practice #1
# Extract the first word of the following sentence using slicing, and display it on the screen:
# "Controlling complexity is the essence of programming"
# Hint: "Controlling" is 11 characters long.
sentence= "Controlling complexity is the essence of programming"
print(sentence.find("controlling"))
print(sentence[0:12])

# Extracting Sub-Strings Practice #2
# Take every third character starting from the ninth to the end of the sentence, and print the result.
# "Never trust a computer you can't throw out a window"
sentence2 = "Never trust a computer you can't throw out a window"
print(sentence2[9::3])
# Extracting Sub-Strings Practice #3
# Reverses the position of all the characters in the following sentence and displays the result on the screen.
# "It's great to work with computers. They don't argue, they remember everything and they don't drink your beer"
sentence3 = "It's great to work with computers. They don't argue, they remember everything and they don't drink your beer"
print(sentence3[::-1])