# Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

# Suppose the following input is supplied to the program: 9

# Then the output should be : 11106


while True:
    number =  input("Please enter a one-digit number : ")
    if len(number) != 1:
        continue
    else :
        one_base = int(number)
        two_base = int(2*number)
        there_base = int(3*number)
        four_base = int(4*number)
        result = one_base + two_base + there_base + four_base
        print(result)