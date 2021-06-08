class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
        self.account_balance += amount	# the specific user's account increases by the amount of the value received
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount

justin = User("Justin","thisjustin.com")
chris = User("Christian","notsochristian.com")
brayan = User("Brayan","wtfudoin.com")

justin.make_deposit(100)
justin.make_deposit(100)
justin.make_deposit(100)
justin.make_withdrawal(130)
justin.display_user_balance()

chris.make_deposit(150)
chris.make_deposit(150)
chris.make_withdrawal(50)
chris.make_withdrawal(50)
chris.display_user_balance()

brayan.make_deposit(300)
brayan.make_withdrawal(75)
brayan.make_withdrawal(75)
brayan.make_withdrawal(75)
brayan.display_user_balance()

justin.transfer_money(brayan,200)
justin.display_user_balance()
brayan.display_user_balance()