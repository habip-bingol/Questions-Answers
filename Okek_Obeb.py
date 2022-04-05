num1 = int(input("enter first number : "))
num2 = int(input("enter second number : "))
obeb = 1 
minimum = min(num1,num2)
for i in range(minimum, 0, -1):
    if num1%i == 0 and num2%i == 0:
        obeb = i 
        break
okek = (num1*num2)/obeb
print(obeb)
print(int(okek))
