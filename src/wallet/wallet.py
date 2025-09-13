
import time

class Wallet:
    def __init__(self):
        self.balance = 200.0  # Default starting balance
        self.transactions = []  # List to store transaction history

    def add_funds(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append({
                'type': 'add_funds',
                'amount': amount,
                'balance': self.balance,
                'timestamp': time.time()
            })
            return True
        return False

    def deduct_zakat(self):
        zakat_amount = self.calculate_zakat()
        if zakat_amount <= self.balance:
            self.balance -= zakat_amount
            self.transactions.append({
                'type': 'deduct_zakat',
                'zakat_amount': zakat_amount,
                'balance': self.balance,
                'timestamp': time.time()
            })
            return zakat_amount
        return 0.0

    def calculate_zakat(self):
        return self.balance * 0.025

    def get_balance(self):
        return self.balance

    def update_balance(self, amount):
        self.balance += amount
        self.transactions.append({
            'type': 'update_balance',
            'amount': amount,
            'balance': self.balance,
            'timestamp': time.time()
        })
        return True