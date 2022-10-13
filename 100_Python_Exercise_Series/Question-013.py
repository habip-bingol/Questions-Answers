# Question:
# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program:
# hello world! 123

# Then, the output should be:
# LETTERS 10
# DIGITS 3

sentence = input("Please enter a sentence : ")
letters = []
digits = []
for i in sentence:
    if i.isdigit():
        digits.append(i)
    elif i.isalpha():
        letters.append(i)
    else:
        pass

print(f"In this sentence There is {len(letters)} letters and {len(digits)} digits.")
