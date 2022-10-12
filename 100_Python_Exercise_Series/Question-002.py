# - Write a program which can compute the factorial of a given numbers.

def factorial(num):
    result  = 1
    for i in range(1, num+1):
        result*=i
    print(result)
number = int(input("Please enter a number : "))
factorial(number)        