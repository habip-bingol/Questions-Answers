X = int(input("Please enter X value :  "))
Y = int(input("Please enter Y value :  "))

result = []
for i in range(X):
    my_list = []
    for j in range(Y):
        multiply = i*j
        my_list.append(multiply)
    result.append(my_list)
    
print(result)
        