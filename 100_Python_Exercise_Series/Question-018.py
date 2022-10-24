# A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:

# At least 1 letter between [a-z]
# At least 1 number between [0-9]
# At least 1 letter between [A-Z]
# At least 1 character from [$#@]
# Minimum length of transaction password: 6
# Maximum length of transaction password: 12

# Your program should accept a passwords and will check it according to the above criteria. if the Password matches the criteria, it will be approved.

# Example : If the following password is given as input to the program: ABd1234@1

# Then, the output of the program should be: APPROVED

# But if the following passwords are given as input to the program:  a F1# / 2w3E* / 2We3345

# Then, the output of the program should be: NOT APPROVED TRY AGAIN PLEASE


password = input("Please enter your password according to the above criteria : "  )

if (len(password)>6) and (len(password)<16):
    if any((i.isupper()) for i in password):
        pass
    else :
        print("NOT APPROVED TRY AGAIN PLEASE")
        
    if any((i.islower()) for i in password):
        pass
    else :
        print("NOT APPROVED TRY AGAIN PLEASE")
    if any((i.isdigit()) for i in password):
        pass
    else :
        print("NOT APPROVED TRY AGAIN PLEASE")
    if any([i in password for i in "$#@"]) :
        print("APPROVED")
    else :
        print("NOT APPROVED TRY AGAIN PLEASE")
           
else :
    print("NOT APPROVED TRY AGAIN PLEASE")