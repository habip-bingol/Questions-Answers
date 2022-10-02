#codewars question
# Define a function that takes in two non-negative integers a and b and returns the last decimal digit of a^b 

lasts= {
    0: [0,0,0,0],   
    1: [1,1,1,1],
    2: [2,4,8,6],
    3: [3,9,7,1],
    4: [4,6,4,6], 
    5: [5,5,5,5], 
    6: [6,6,6,6], 
    7: [7,9,3,1], 
    8: [8,4,2,6], 
    9: [9,1,9,1], 
}

def last_digit(a, b):
    if b == 0:
        return 1
    else:
        last_a = int(str(a)[-1])  # last digit of first number (a)
        digit = lasts[last_a]     # according to the last digit, which list I will choose in lasts dict
        return digit[(b % 4) - 1] # the values ​​repeat every four times;
last_digit(2 **200, 2 ** 300)
