# Define a class with a generator which can iterate the numbers, 
# which are divisible by 7, between a given range 0 and n

def divide(n):
    my_list=[]
    for i in range(n):
        if i%7 == 0 :
            my_list.append(i)
        
    return my_list

divide(100)