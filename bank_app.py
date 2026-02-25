from bank_fi import Bank
import random

account = None

def createAcc():
    print('Create New Bank Account')
    print('-----------------------')
    global account
    account = Bank(
        random.randint(10000000,999999999),
        input('Enter Account Holder Name: '),
        int(input("Enter Initial Deposit: "))
    )
    print('A new bank account is created!')
createAcc()

def display_Menu():
    print('Choose Your Operation')
    print('---------------------')
    print('1.Profile')
    print('2.Deposit')
    print('3.Withdraw')
    print('4.Exist')

while True:
    display_Menu()
    ans = input('Enter your choice: ').lower()
    if ans == '1' or ans == 'profile':
        account.accInfo()
    elif ans == '2' or ans == 'deposit':
        amount = int(input('Enter Deposit Amount: '))
        account.deposit(amount)
    elif ans == '3' or ans == 'withdraw':
        amount = int(input('Enter Withdraw Amount: '))
        account.withdraw(amount)
    else:
        break
