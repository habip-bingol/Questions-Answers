#Write a function named `freq(l)` that takes a list `l` of numbers and returns a list of the most frequent number and its frequency.
#For example, `freq([1,2,3,4,5,2,3,4,5,3,4,5,4,5,4]) returns [4,5] because number 4 appears 5 times in this list. If multiple numbers
#appear as most frequent, then the first element of the returned list is a list of all those numbers.

#For example, freq([1,2,3,1,2,1,2,3,1,2]) will return [[1,2], 4]


def frequent(list1):
    my_dict = {}
    for i in list1:
        my_dict[i] = list1.count(i)
    print(my_dict)
    maxi = max(my_dict.values())
    most_repeated = [k for k ,v in my_dict.items() if v == maxi] 
    
    return [most_repeated, maxi ]
#frequent([1,2,3,1,2,1,2,3,1,2])
#[[1, 2], 4]
