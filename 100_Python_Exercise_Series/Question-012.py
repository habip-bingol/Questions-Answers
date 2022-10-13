# Question:
# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of
# the number is an even number.

# The numbers obtained should be printed in a comma-separated sequence on a single line.

new_list =[] 
for a in range(1000,3001):
    for b in str(a):
        if int(b) % 2 == 1:
            break
    else:
        new_list.append(a)
new_list        