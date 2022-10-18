# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.

# Suppose the following input is suppliled to the program: Hello world!

# Then the output should be :
# UPPER CASE : 1
# LOWER CASE : 9


sentence = input("Please enter a sentence : ")
upper_count = 0
lower_count = 0
for i in sentence:
    if i.isupper():
        upper_count+=1
    elif i.islower():
        lower_count+=1
    else :
        pass

print(f"UPER CASE : {upper_count}\nLOWER CASE : {lower_count}")
    