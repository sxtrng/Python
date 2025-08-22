class Account:
    def __init__(self, initial):
        self.balance = initial

    def display_balance(self):
        print('Balance', self.balance)

    def __add__(self, other):
        total = self.balance + other.balance
        return Account(total)


account_one = Account(50)
account_two = Account(10)

new_account = account_one + account_two
new_account.display_balance()