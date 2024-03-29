# You are required to write a program to sort the (name, age, score) tuples by ascending order where name is string, age and score are numbers. The tuples are input by console. The sort criteria is:
# 1: Sort based on name;
# 2: Then sort based on age;
# 3: Then sort by score.

# The priority is that name > age > score.

# If the following tuples are given as input to the program:

# Tom,19,80
# John,20,90
# Jony,17,91
# Jony,17,93
# Json,21,85

# Then, the output of the program should be:
# [(John’, '20', '90'), (‘Jony’, '17', '91'), (Jony’, '17', '93°), (‘Json’, '21', '85'), ‘Tom’, ‘19’, '80')]


from operator import itemgetter

person_list = []

while True :
    if input("Do you want to continue : ") != "yes":
        break
    else:
        person = ()
        name = input("Enter a name please : ")
        age = int(input("Enter the age please :"))
        score = int(input("Enter the score please : "))
        person = (name, age, score)
        person_list.append(person,)



person_list.sort(key =  itemgetter(0, 1, 2))       
print(person_list)


# or we can sort list like following way
# print(sorted(person_list, key=lambda x: (x[0], x[1], x[2])))

