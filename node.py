class Node:
    def __init__(self, wallet):
        self.wallet = wallet
        self.blockchain = Blockchain()

    def create_transaction(self, recipient, amount):
        transaction = Transaction(self.wallet.address, recipient, amount)
        self.blockchain.add_transaction(transaction)
