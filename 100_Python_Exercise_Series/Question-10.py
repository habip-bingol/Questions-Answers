# Write a program that accepts a sequence of whitespace seperated words as input and prints the words after removing all duplicatd words and sorting them alphabetically.

# Suppose the following input is supplied to the program :
# hello world and practice makes perfect and hello world again

# Then the output should be :
# again and hello makes perfect practice world


sentences = input("Please enter a sentence : ")
sentences = sentences.split(" ")

print(" ".join(sorted(sentences)))
