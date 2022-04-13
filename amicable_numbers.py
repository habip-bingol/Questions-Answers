# Write the amicable numbers from 1 to 10000
# Amicable numbers are two different natural numbers related in such a way 
# that the sum of the proper divisors of each is equal to the other number.

def divisions_sum(n):
    div_list = []
    total = 0
    i = 1
    while i < (n/2+1):
        if n % i == 0:
            total += i
        i += 1
    return total

amicable = []
for a in range(1, 10000):
    for b in range(1, 10000):
        if divisions_sum(a) == b and divisions_sum(b) == a and a != b:
            amicable.append([a,b])
            print(amicable)

