import hashlib
import time
from transaction import Transaction

class Block:
    def __init__(self, index, previous_hash, transactions, timestamp=None):
        self.index = index
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.timestamp = timestamp or time.time()
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.previous_hash}{self.transactions}{self.timestamp}".encode()
        return hashlib.sha256(block_string).hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.create_block(previous_hash='1')  # Genesis block

    def create_block(self, previous_hash):
        block = Block(len(self.chain) + 1, previous_hash, self.current_transactions)
        self.current_transactions = []
        self.chain.append(block)
        return block

    def add_transaction(self, transaction):
        self.current_transactions.append(transaction)

    def get_last_block(self):
        return self.chain[-1]
