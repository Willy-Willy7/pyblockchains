def print_blockchain(blockchain):
    for block in blockchain.chain:
        print(f"Block {block.index} Hash: {block.hash} Transactions: {block.transactions}")
