# Define a function which can generate a list where the values are square of numbers between 1 and 20 (both included). 
# Then the function needs to print all values except the first 5 elements in the list.


def square_list():
    squares = []
    for i in range(1,21):
        squares.append(i**2)
    print(squares[5:])
        
    
square_list()            