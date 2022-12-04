# Define a function that can accept two strings as input and print the string with maximum length in console. 
# If two strings have the same length, then the function should print all strings line by line.


def len_calc(s1, s2):
    if len(s1) > len(s2):
        print(s1)
    elif len(s2) > len(s1):
        print(s2)
    else:
        print(s1)
        print(s2)
        
        
# len_calc("one", "two")       # both of them
# len_calc("one", "three")     # second one
# len_calc("four", "one")      # first one 
