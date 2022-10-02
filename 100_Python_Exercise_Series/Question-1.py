# Write a program  which will find all such numbers which are divisible by 7 
# but are not a multiple of5, between 200 and 3200 (both included)

my_list = []
for i in range(2000, 3201):
    if (i%7==0) and (i%5!=0):
        my_list.append(i)
print(my_list )       