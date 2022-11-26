# Python has many built-in functions, and if you do not know how to use it, you can read document online or find some books. 
# But Python has a built-in document function for every built-in functions.

# Please write a program to print some Python built-in functions documents, such as abs(), input() etc.

# And add document for your own function


# first part
print(abs.__doc__)
print(input.__doc__)

# second part
def square(num):
    '''Return the square value of the input number.

    The input number must be integer.'''
    return num**2

print (square(2))
print(square.__doc__)