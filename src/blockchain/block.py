
import hashlib
import time

class Block:
    def __init__(self, index, transactions, previous_hash, roll_number):
        self.index = index
        self.transactions = transactions
        self.previous_hash = previous_hash
        self.timestamp = self.get_timestamp()
        self.roll_number = roll_number
        self.hash = self.calculate_hash()

    def get_timestamp(self):
        return int(time.time())

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.transactions}{self.previous_hash}{self.roll_number}"
        # Use roll_number as seed in hash
        hash_obj = hashlib.sha256()
        hash_obj.update(str(self.roll_number).encode())
        hash_obj.update(block_string.encode())
        return hash_obj.hexdigest()

    # Removed duplicate methods. Only the correct get_timestamp and calculate_hash remain above.