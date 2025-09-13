class Miner:
    def __init__(self, blockchain):
        self.blockchain = blockchain

    def mine_block(self, transactions):
        previous_block = self.blockchain.get_last_block()
        new_block = self.blockchain.create_block(transactions, previous_block.hash)
        self.blockchain.add_block(new_block)
        return new_block

    def validate_chain(self):
        return self.blockchain.is_chain_valid()