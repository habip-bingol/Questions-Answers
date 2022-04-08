# Write a function named `vectorSum(l1, l2)` that takes two lists of numbers and adds the numbers in l2 on l1, one by one. 
# If l2 is shorter than l1, then l2 recycles from the beginning once it is over. If l2 is longer than l1,
# then only the first part of l2 that matches the length of l1 is considered. Your function must return the summed up resulting list.

# For example, vectorSum([1,2,3,4,5], [1,2,3]) returns [2,4,6,5,7] //vectorSum([1,2,3], [1,2,3,4,5]) returns [2,4,6] // 
#vectorSum([1,2,3,4,5], [1,2,1,2,1]) returns [2,4,4,6,6]


def vectorSum(l1, l2):
    len_fark = len(l1)-len(l2)
    new_list = []
    if len(l1) > len(l2):
        for i in range(0,len_fark):
            l2.append(l1[i])
        
        for i in range(0,len(l1)):
            new_list.append(l1[i] + l2[i])
        return new_list

    elif len(l1) < len(l2):
        for i in range(0,len(l1)):
            new_list.append(l1[i] + l2[i])
        return new_list
    
    else :
        for i in range(0,len(l1)):
            new_list.append(l1[i] + l2[i])
        return new_list

