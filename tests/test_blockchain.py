from src.blockchain.blockchain import Blockchain
from src.blockchain.block import Block
from src.blockchain.transaction import Transaction
import unittest

class TestBlockchain(unittest.TestCase):

    def setUp(self):
        self.blockchain = Blockchain()

    def test_add_block(self):
        transaction = Transaction(sender="rao", receiver="saim", deducted_zakat=10, remaining_balance=390, timestamp="2023-10-01")
        block = Block(transactions=[transaction], previous_hash="0")
        self.blockchain.add_block(block)
        self.assertEqual(len(self.blockchain.chain), 1)
        self.assertEqual(self.blockchain.chain[0].transactions[0].sender, "rao")

    def test_validate_chain(self):
        transaction1 = Transaction(sender="rao", receiver="saim", deducted_zakat=10, remaining_balance=390, timestamp="2023-10-01")
        block1 = Block(transactions=[transaction1], previous_hash="0")
        self.blockchain.add_block(block1)

        transaction2 = Transaction(sender="Saim", receiver="rao", deducted_zakat=5, remaining_balance=385, timestamp="2023-10-02")
        block2 = Block(transactions=[transaction2], previous_hash=block1.hash)
        self.blockchain.add_block(block2)

        self.assertTrue(self.blockchain.validate_chain())

    def test_invalid_chain(self):
        transaction1 = Transaction(sender="mubashir", receiver="saim", deducted_zakat=10, remaining_balance=390, timestamp="2023-10-01")
        block1 = Block(transactions=[transaction1], previous_hash="0")
        self.blockchain.add_block(block1)

        # Manually tampering with the blockchain
        self.blockchain.chain[0].transactions[0].deducted_zakat = 20

        self.assertFalse(self.blockchain.validate_chain())

if __name__ == '__main__':
    unittest.main()