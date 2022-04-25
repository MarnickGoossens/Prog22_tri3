class Grouping:
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0

    def __repr__(self):
        string = self.name.center(30, "*")
        for dic in self.ledger:
            for key, value in dic.items():
                pass
        return string

    def print_ledger(self):
        print(self.ledger)

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

    def transfer(self, amount, group):
        group.withdraw(amount, "transfer")
        self.deposit(amount)

    def check_funds(self, amount):
        if self.balance < amount:
            return False
        else:
            return True


def create_spend_chart(groups):
    pass


kleren = Grouping("kleren")
kleren.deposit(1000, "first deposit")
kleren.withdraw(100, "j&j")
kleren.print_ledger()
