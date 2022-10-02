#Create a function that takes a positive integer and returns the next bigger number that can be formed by rearranging its digits.
#  For example:
def next_bigger(number):
    if (sorted(str(number), reverse= True) == list(str(number))):
        return -1
    else :
        result = number
        while True:
            result += 1
            if sorted(str(result)) == sorted(str(number)):
                return result
                break
#next_bigger(12) // returns 21
#next_bigger(513) // returns 531
#next_bigger(2017) // returns 2071           