class Bankaccount:
    def __init__(self,account_number,owner_name,balance):
        self.account_number=account_number
        self.owner_name=owner_name
        self.balance=balance

    def check_balance(self):
        print(f"Your current balance is {self.balance}")
    
    def deposit(self, amount):
        self.balance+=amount
    def withdraw(self,amount):
        print("your money is withdrawn")
        self.balance-=amount


a=Bankaccount(123,"Suyash",40000)
print(a.check_balance())

a.deposit(10000)
print(a.check_balance())
a.withdraw(4000)
print(a.check_balance())
