class Bank:
    # accno = 0
    # name = ""
    # balance = 0 doesn't need anymore.

    def __init__(self,accno,name,balance):
        self.accno = accno
        self.name = name
        self.balance = balance
    def accInfo(self):
        print('Bank Accound Information')
        print('========================')
        print(f'Account No \t:{self.accno}')
        print(f'Name\t\t:{self.name}')
        print(f'Balance\t\t:${self.balance}')
        print('----------------------')

    def deposit(self,amount):
        self.balance += amount
        print(f'${amount} is successfully deposited!')
        print(f'Now your balance is ${self.balance}.')
        print('----------------------------')

    def withdraw(self,amount):
        print(f'Total Balance:\t\t{self.balance}\nWithdraw amount:\t{amount}')

        if amount >= self.balance:
            print("Insufficient Balance!!")
        else :
            self.balance -= amount
            print(f"Remaining Balance is {self.balance}")
        print('-------------------------')






# acc1 = Bank(10010011,"jante",10000000)
# acc1.accInfo()