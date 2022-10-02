# With a given integral number n , write a program to generate a dictionary that
# contains (i, i*i) such that is an integral number between 1 and n (both included). 
# And then the program should print the dictionary

my_dict = {}

number = int(input("Please enter a number : "))

for i in range(1, number+1):
    my_dict[i] = i*i

print(my_dict)
