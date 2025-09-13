# filepath: /zakat-blockchain-simulation/zakat-blockchain-simulation/src/zakat/rules.py

class ZakatRules:
    def log_transaction(self, balance, zakat):
        # Dummy implementation for testing
        return f"Zakat deducted: {zakat} from balance: {balance}"
    def __init__(self):
        self.zakat_rate = 0.025  # Zakat is 2.5%
        self.minimum_nisab = 1  # Define the minimum amount for Zakat eligibility

    def is_eligible_for_zakat(self, balance):
        """
        Check if the balance meets the nisab threshold for Zakat eligibility.
        """
        return balance >= self.minimum_nisab

    def calculate_zakat(self, balance):
        """
        Calculate the Zakat amount based on the balance.
        """
        if self.is_eligible_for_zakat(balance):
            return balance * self.zakat_rate
        return 0

    def distribution_guidelines(self):
        """
        Provide guidelines on how Zakat should be distributed.
        """
        return {
            "eligible_recipients": [
                "the poor",
                "the needy",
                "those employed to collect Zakat",
                "those whose hearts are to be reconciled",
                "to free the captives",
                "those in debt",
                "in the cause of Allah",
                "the wayfarer"
            ],
            "distribution_method": "Zakat should be distributed directly to eligible recipients."
        }