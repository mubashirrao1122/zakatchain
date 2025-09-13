

import time
from blockchain.block import Block

class Blockchain:
    def __init__(self, roll_number):
        self.chain = []
        self.current_transactions = []
        self.roll_number = roll_number
        # Create the genesis block
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(
            index=1,
            transactions=[],
            previous_hash='1',
            roll_number=self.roll_number
        )
        self.chain.append(genesis_block)

    def new_block(self, transactions):
        previous_block = self.chain[-1]
        block = Block(
            index=len(self.chain) + 1,
            transactions=transactions,
            previous_hash=previous_block.hash,
            roll_number=self.roll_number
        )
        self.chain.append(block)
        return block

    def add_transaction(self, sender, receiver, zakat_deducted, remaining_balance):
        transaction = {
            'sender': sender,
            'receiver': receiver,
            'zakat_deducted': zakat_deducted,
            'remaining_balance': remaining_balance,
            'timestamp': int(time.time()),
        }
        self.current_transactions.append(transaction)
        return len(self.chain) + 1


    @property
    def last_block(self):
        return self.chain[-1]

    def hash(self, block):
        return block.hash

    def validate_chain(self):
        for i in range(1, len(self.chain)):
            previous = self.chain[i - 1]
            current = self.chain[i]
            if current.previous_hash != previous.hash:
                return False
            # Hash is already validated by construction
        return True