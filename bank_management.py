import random
import math

class Transaction:
    def __init__(self , trans_id , trans_amount ,  trans_type , message):
        self.trans_id = trans_id
        self.trans_amount = trans_amount
        self.trans_type = trans_type
        self.message = message

class Account:
    def __init__(self , acc_number , acc_holder_name , password , balance=0):
        self.acc_number = acc_number
        self.acc_holder_name = acc_holder_name,
        self.balance = balance
        self.password = password
        self.transactions = []
        if balance > 0:
            random_number = math.floor(random.random() * 10000)
            transaction = Transaction(random_number , balance, "Account Opening" , "Opening Balance Success")
            self.transactions.append(transaction)

    def deposit(self , balance):
        self.balance += balance
        random_number = math.floor(random.random() * 10000)
        print(random_number)
        transaction = Transaction(random_number , balance , "Deposit" , "Deposit Success")
        self.transactions.append(transaction)
        print("Deposit Success")

    def withdraw(self , password , balance):
        if self.password != password:
            print("Wrong Password")
            return

        if self.balance < balance:
            print("Insufficient Balance")
            return

        self.balance -= balance
        random_number = math.floor(random.random() * 10000)
        transaction = Transaction(random_number , balance , "Withdraw" , "Withdraw Success")
        self.transactions.append(transaction)
        print("Withdraw Success")

    def printBalance(self , acc_no , password):
        if self.password != password:
            print("Wrong Password")
            return
        print(self.balance)
        for transaction in self.transactions:
            print(transaction.trans_type + " And Balance is " + str(transaction.trans_amount))

class Bank:
    def __init__(self):
        self.accounts = []

    def createAccount(self):
        acc_id = math.floor(random.random() * 10000)
        acc_holder_name = input("Enter You Name")
        password = input("Enter Password")
        balance = int(input("Enter balance"))
        account = Account(acc_id , acc_holder_name , password , balance)
        print(account.acc_number)
        self.accounts.append(account)

    def deposit(self, acc_no , balance):
        acc = None
        for account in self.accounts:
            if account.acc_number == acc_no:
                acc = account
        acc.deposit(balance)

    def printBalance(self ,acc_no , password):
        acc = None
        for account in self.accounts:
            if account.acc_number == acc_no:
                acc = account
        acc.printBalance(acc_no , password)

    def withdraw(self , acc_no , password , balance):
        acc = None
        for account in self.accounts:
            if account.acc_number == acc_no:
                acc = account
            acc.withdraw(password , balance)



bank = Bank()

print("Press 1 For Create Account")
print("Press 2 For Deposit Money")
print("Press 3 Fror Withdraw Money")
print("Press 4 For view All Transactions")
choice = None
while choice !=5 :
    choice = int(input("Enter Your CHoice"))
    match(choice):
        case 1:
            bank.createAccount()

        case 2:
            acc_no = int(input("Enter Account Number"))
            balance = int(input("Enter The Blance"))
            bank.deposit(acc_no , balance)

        case 3:
            acc_no = int(input("Enter Account Number"))
            password = input("Enter Password")
            balance = int(input("Enter Balance"))
            bank.withdraw(acc_no , password , balance)

        case 4:
            acc_no = int(input("Enter Account Number"))
            password = input("Enter Password")
            bank.printBalance(acc_no , password)
        case 5:
            break

        