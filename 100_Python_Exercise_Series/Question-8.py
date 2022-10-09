# Write a program that accepts a comma seperated sequence of words as input and prints the words in a comma-seperated sequence after sorting them alphabeticallay. 

# Suppose the following input is supplied to the program:
# without, hello, bag, world

# Then output should be: 
# bag, hello,without,world



word_list = input().split(",")

word_list.sort()
for i in word_list:
    print(i)

    
# second way    

# word_list = input().split(",")
# sorted(word_list)
    