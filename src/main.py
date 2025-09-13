from blockchain.blockchain import Blockchain
from wallet.wallet import Wallet
from zakat.calculator import calculate_zakat

def main():
    # Set your roll number here (as a string or int)
    roll_number = "22p-9063" 
    # Initialize the blockchain with roll number
    zakat_blockchain = Blockchain(roll_number)

    # Initialize wallets for users
    user_wallets = {
        "Mubashir": Wallet(),
        "Saim": Wallet(),
    }

    # Example transactions
    transactions = [
        {"sender": "Mubashir", "receiver": "Saim", "amount": 100},
        {"sender": "Saim", "receiver": "Mubashir", "amount": 50},
    ]

    # Process transactions and add to blockchain
    for tx in transactions:
        sender = user_wallets[tx["sender"]]
        receiver = user_wallets[tx["receiver"]]

        # Deduct Zakat from sender's wallet
        zakat_amount = sender.deduct_zakat()

        # Update balances
        sender.update_balance(-tx["amount"])
        receiver.update_balance(tx["amount"])

        # Add transaction to blockchain
        zakat_blockchain.add_transaction(
            sender=tx["sender"],
            receiver=tx["receiver"],
            zakat_deducted=zakat_amount,
            remaining_balance=sender.get_balance()
        )

    # Add all transactions as a new block
    zakat_blockchain.new_block(zakat_blockchain.current_transactions)

    # Display the blockchain
    for block in zakat_blockchain.chain:
        print(f"Block {block.index} - Hash: {block.hash}")
        for t in block.transactions:
            print(t)

if __name__ == "__main__":
    main()