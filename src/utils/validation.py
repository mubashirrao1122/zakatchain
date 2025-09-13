def validate_block(block, previous_block):
    if previous_block is None:
        return True  # The first block is always valid

    if block.previous_hash != previous_block.hash:
        return False  # The previous hash must match

    if not isinstance(block.transactions, list):
        return False  # Transactions must be a list

    # Additional validation rules can be added here
    return True

def validate_chain(blockchain):
    for i in range(1, len(blockchain)):
        if not validate_block(blockchain[i], blockchain[i - 1]):
            return False
    return True

def validate_transaction(transaction):
    required_fields = ['sender', 'receiver', 'deducted_zakat', 'remaining_balance', 'timestamp']
    for field in required_fields:
        if field not in transaction:
            return False  # All required fields must be present
    return True