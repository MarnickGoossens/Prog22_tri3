class Grouping:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0

    def deposit(self, amount, description=""):
        self.balance += amount
        dictionary = {description: amount}
        self.ledger.append(dictionary)

    def withdraw(self, amount, description=""):
        if self.balance < amount:
            return False
        elif self.balance > amount:
            self.balance -= amount
            dictionary = {description: amount}
            self.ledger.append(dictionary)
            return True

    def get_balance(self):
        return self.balance

    def transfer(self):
        pass

    def check_funds(self, amount):
        if self.balance < amount:
            return False
        else:
            return True


def create_spend_chart(groups):
    pass
