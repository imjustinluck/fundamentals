class User:
    def __init__(self, name, email):
        self.accounts = []
        self.name = name
        self.email = email
    def make_new_account(self, int_rate=0.02, balance=0):
        new_acc = BankAccount(int_rate, balance)
        self.accounts.append(new_acc)
    def transfer_money(self, other_user, amount):
        self.account.balance -= amount
        other_user.account.balance += amount


class BankAccount:
    all_inst = []
    def __init__(self,int_rate=0.01,balance=0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_inst.append(self)
    def deposit(self,amount):
        self.balance += amount
        return self
    def withdraw(self,amount):
        if (amount>self.balance):
            self.balance-=5
            self.balance-=amount
            return self
        else:
            self.balance-=amount
            return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        if self.balance>0:
            self.balance*=(self.int_rate+1)
        return self
    @classmethod
    def inst_print(cls):
        for account in cls.all_inst:
            print(account.balance)

Joe = User("Joe","joemama")
Joe.make_new_account(0.1,100)
Joe.make_new_account(.2,2000)
print(Joe.accounts)

Joe.accounts[1].deposit(100).display_account_info()



        # self.account = BankAccount(int_rate=0.02,balance=0)
    # def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    #     self.account.balance += amount	# the specific user's account increases by the amount of the value received
    # def make_withdrawal(self, amount):
    #     self.account.balance -= amount
    # def display_user_balance(self):
    #     print(f"User: {self.name}, Balance: ${self.account.balance}")



# acc1 = BankAccount()
# acc2 = BankAccount()

# acc1.deposit(100).deposit(50).deposit(25).withdraw(100).display_account_info()
# acc2.deposit(600).deposit(50).withdraw(100).withdraw(100).withdraw(100).withdraw(100).display_account_info()

# # NINJA BONUS: use a classmethod to print all instances of a Bank Account's info

# BankAccount.inst_print()