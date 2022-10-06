# Write a program that calculates and prints the value according to the given formula :
# Q = Square root of [(2 * C * D )/H]
# Following are the fixed values of C and H :
# C is 50. H is 30.
# D is variable whose values should be input to your program in a comma-seperated sequence.
# Example :
# Let us assume the following comma-seperated input sequence is given to the program : 100,150,180
# The output of the program should be : 18,22,24


import math
c = 50
h = 30 
d = input().split(",")

values = []

for i in d:
    i = int(i)
    result = round(math.sqrt((2*c*i)/h))
    values.append(result)
    
print(values)