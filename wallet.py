import uuid

class Wallet:
    def __init__(self):
        self.address = str(uuid.uuid4())
        self.balance = 0

    def add_balance(self, amount):
        self.balance += amount

    def subtract_balance(self, amount):
        self.balance -= amount
