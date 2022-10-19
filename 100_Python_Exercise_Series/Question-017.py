# Write a program that computes the net amount of a bank account based a transaction log from console input. The transaction log format is shown as following:

# D 100
# W 200

# D means deposit while W means withdrawal.

# Suppose the following input is supplied to the program:
# D 300
# D 300
# W 200
# D 100

# Then, the output should be: 500

net_amount = 0
while True : 
    process = input("Tell me what will you do please (D/W): ")
    if (process != "D") and (process != "W"):
        print(net_amount)
        break
    elif process == "D" :
        deposit = int(input("How much is your deposit amount : "))
        net_amount+=deposit
    elif process == "W" :
        withdrawal = int(input("How much is your withdrawal amount : "))
        net_amount-=withdrawal
        
# (input type slightly modified according to the scenario)