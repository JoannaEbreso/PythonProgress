print("Please enter your name: ")
name=input()

balance=3000
depositCount=0
withdrawalCount=0
totalDeposit=0
totalWithdrawal=0

print("What do you want to do? Press 1 for deposit, 2 for withdrawal and 3 to exit ")
number=int(input())
while number!=3:
    if number==1:
        print("How much do you want to deposit? ")
        deposit=int(input())
        if deposit>0:
            balance = balance + deposit
            depositCount+=1
            totalDeposit = totalDeposit + deposit
            print("done!")
        else:
            print("You can't deposit 0 or less")
        print("What else do you want to do? Press 1 for deposit, 2 for withdrawal and 3 to exit ")
        number=int(input())

    elif number==2:
        print("How much do you want to withdraw? ")
        withdraw=int(input())
        if withdraw<=balance:
            balance = balance - withdraw
            withdrawalCount+=1
            totalWithdrawal = totalWithdrawal + withdraw
            print("done!")
        else:
            print("You can't withdraw more than what you have ")
        print("What else do you want to do? Press 1 for deposit, 2 for withdrawal and 3 to exit ")
        number=int(input())
        
print("TRANSACTION SUMMARY")
print("Account Name: {}". format(name))
if depositCount!=0:
    print("Number of times you Deposited: {}". format(depositCount))
    print("Total Amount Deposited: {}". format(totalDeposit))

if withdrawalCount!=0:
    print("Number of times you withdrew: {}". format(withdrawalCount))
    print("Total Amount Withdrawn: {}". format(totalWithdrawal))
        
    
