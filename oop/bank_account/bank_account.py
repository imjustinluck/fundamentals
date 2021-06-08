class BankAccount:
    all_inst = []
    def __init__(self,balance=0,int_rate=0.01):
        self.balance = balance
        self.int_rate = int_rate
        BankAccount.all_inst.append(self)
    def deposit(self,amount):
        self.balance += amount
        print(f"This what you got! {self.balance}!")
        return self
    def withdraw(self,amount):
        if (amount>self.balance):
            self.balance-=5
            self.balance-=amount
            print(f"Insufficient Funds: Charging a $5 Fee. You got {self.balance} buckaroos ):")
            return self
        else:
            self.balance-=amount
            print(f"Here's your new amount! {self.balance}!")
            return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        if self.balance>0:
            self.balance*=(self.int_rate+1)
            print(f"Here's your new balance with some interest! {self.balance}")
        return self
    @classmethod
    def inst_print(cls):
        for account in cls.all_inst:
            print(account.balance)

acc1 = BankAccount()
acc2 = BankAccount()

acc1.deposit(100).deposit(50).deposit(25).withdraw(100).display_account_info()
acc2.deposit(600).deposit(50).withdraw(100).withdraw(100).withdraw(100).withdraw(100).display_account_info()

# NINJA BONUS: use a classmethod to print all instances of a Bank Account's info

BankAccount.inst_print()