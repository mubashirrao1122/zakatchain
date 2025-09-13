class Transaction:
    def __init__(self, sender, receiver, deducted_zakat, remaining_balance):
        self.sender = sender
        self.receiver = receiver
        self.deducted_zakat = deducted_zakat
        self.remaining_balance = remaining_balance
        self.timestamp = self.get_timestamp()

    def get_timestamp(self):
        from datetime import datetime
        return datetime.now().isoformat()

    def to_dict(self):
        return {
            'sender': self.sender,
            'receiver': self.receiver,
            'deducted_zakat': self.deducted_zakat,
            'remaining_balance': self.remaining_balance,
            'timestamp': self.timestamp
        }