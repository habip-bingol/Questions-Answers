# Question:
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check
# whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated
# sequence.

# Example:
# 0100,0011,1010,1001

# Then the output should be:
# 1010


numbers = input().split(",")
for i in numbers:
    summ=0
    base = 0
    int_i = int(i)
    for j in range(len(i)):
        summ = summ + (int_i%10)*(2**(base))
        base+=1
        int_i=int_i//10 
    if summ%5==0:
        print(i)

