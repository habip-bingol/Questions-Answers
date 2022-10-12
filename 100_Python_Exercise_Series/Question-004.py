# Write a program which accepts a sequence of comma-separated numbers from console and
# generate a list and a tuple which contains every number

# Suppose the following input is supplied to the program:
# 34, 67,55,33,12,98

# Then the output should be : 
# "34", "67", "33", "12", "98"

numbers_list = []
number = True
while number != "ok".lower():
    number = input("Enter a number : ")
    if number == "ok".lower():
        break
    numbers_list.append(number)
print(numbers_list)
print(tuple(numbers_list))