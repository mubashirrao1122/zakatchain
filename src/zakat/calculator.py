def calculate_zakat(balance):
    """
    Calculate Zakat based on the given balance.
    Zakat is 2.5% of the balance.
    """
    if balance < 0:
        raise ValueError("Balance cannot be negative.")
    zakat_amount = balance * 0.025
    return zakat_amount

def record_deduction(balance):
    """
    Deduct Zakat from the balance and return the remaining balance.
    """
    zakat_amount = calculate_zakat(balance)
    remaining_balance = balance - zakat_amount
    return remaining_balance, zakat_amount