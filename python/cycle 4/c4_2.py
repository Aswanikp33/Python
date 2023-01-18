class BankAccount:
    def __init__(self):
        self.accno=int(input("Enter the account number:"))
        self.name=input("Enter the name:")
        self.account_type=input("Enter account type:")
        self.balance=0
    def deposit(self,amount):
        self.balance=self.balance+amount
        return self.balance
    def withdraw(self,amount):
        try:
            if(self.balance<amount):
                print("Insufficent balance")
            else:
                self.balance=self.balance-amount
                return self.balance
        except:
            print("Oops..!!Something went wrong")
obj1=BankAccount()
amount1=int(input("Enter the amount deposit:"))
print("Account balance after deposit",obj1.deposit(amount1))
amount2=int(input("Enter the amount to be withdraw:"))
print("Account balance after withdrawel",obj1.withdraw(amount2))
