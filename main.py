from wallet import Wallet
from node import Node
from miner import Miner
from network import Network
from utils import print_blockchain

def main():
    # Create wallets
    wallet1 = Wallet()
    wallet2 = Wallet()

    # Create nodes
    node1 = Node(wallet1)
    node2 = Node(wallet2)

    # Create network
    network = Network()
    network.add_node(node1)
    network.add_node(node2)

    # Create a transaction
    node1.create_transaction(wallet2.address, 10)

    # Mine the transaction
    miner = Miner(node1)
    miner.mine()

    # Print the blockchain
    print_blockchain(node1.blockchain)

if __name__ == "__main__":
    main()
