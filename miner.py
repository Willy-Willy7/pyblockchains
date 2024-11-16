class Miner:
    def __init__(self, node):
        self.node = node

    def mine(self):
        last_block = self.node.blockchain.get_last_block()
        new_block = self.node.blockchain.create_block(last_block.hash)
        print(f"Block mined: {new_block.index} with hash: {new_block.hash}")
