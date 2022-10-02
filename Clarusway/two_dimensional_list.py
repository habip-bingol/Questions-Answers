# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional list. 
# The element value in the i-th row and j-th column of the array should be i*j.
# Note: i=0,1.., X-1; j=0,1,¡Y-1.
#  Example
# Suppose the following inputs are given to the program: 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]


x = int(input("enter a number :"))
y = int(input("enter a number : "))
my_list = []
for i in range(x):
    empty = []
    for j in range(y):
        empty.append(i*j)
    my_list.append(empty)

print(my_list)

