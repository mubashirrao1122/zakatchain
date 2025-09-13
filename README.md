---

## How to Run
1. Set your unique identifier in `main.py`:
   ```python
   roll_number = "XXXXX"  # Change to your unique identifier
   ```
2. Run the simulation:
   ```sh
   python src/main.py
   ```

---

## Notes
- All logic is implemented using only lists and dictionaries.
- Each block's hash is unique to the student node due to the roll number seed.
- The blockchain is immutable: any tampering is detectable by hash mismatch.
- All transactions and Zakat deductions are fully traceable and transparent.

---

## Contact
For questions or contributions, please open an issue or pull request.
---

## File & Function Descriptions

### `src/main.py`
- **main()**: Entry point. Initializes blockchain and wallets, processes transactions, deducts Zakat, adds transactions to the blockchain, and prints the chain.

### `src/wallet/wallet.py`
- **Wallet**: Class for managing a user's balance and Zakat.
   - `__init__()`: Initializes wallet with 200 coins and empty transaction history.
   - `add_funds(amount)`: Adds funds to the wallet and logs the transaction.
   - `deduct_zakat()`: Deducts 2.5% Zakat from the balance and logs the deduction.
   - `calculate_zakat()`: Returns 2.5% of the current balance.
   - `get_balance()`: Returns the current balance.
   - `update_balance(amount)`: Updates the balance by the given amount and logs the update.

### `src/zakat/calculator.py`
- **calculate_zakat(balance)**: Returns 2.5% of the given balance.
- **record_deduction(balance)**: Deducts Zakat from balance and returns (remaining_balance, zakat_amount).

### `src/blockchain/block.py`
- **Block**: Class representing a block in the blockchain.
   - `__init__(index, transactions, previous_hash, roll_number)`: Initializes block with index, transactions, previous hash, timestamp, roll number, and computes hash.
   - `get_timestamp()`: Returns the current timestamp.
   - `calculate_hash()`: Computes the block's hash using SHA-256 and roll number as seed.

### `src/blockchain/blockchain.py`
- **Blockchain**: Class managing the chain of blocks.
   - `__init__(roll_number)`: Initializes the blockchain with the student's roll number and creates the genesis block.
   - `create_genesis_block()`: Creates the first block in the chain.
   - `new_block(transactions)`: Adds a new block with the given transactions.
   - `add_transaction(sender, receiver, zakat_deducted, remaining_balance)`: Adds a transaction to the current transaction list.
   - `last_block`: Returns the last block in the chain.
   - `hash(block)`: Returns the hash of a block.
   - `validate_chain()`: Validates the blockchain's integrity by checking hashes.

### `src/blockchain/transaction.py`
- **Transaction**: Class for transaction data.
   - `__init__(sender, receiver, deducted_zakat, remaining_balance)`: Initializes a transaction.
   - `get_timestamp()`: Returns the transaction timestamp.
   - `to_dict()`: Returns transaction as a dictionary.

## Project Structure
zakat-blockchain-simulation
├── src
│   ├── blockchain
│   │   ├── __init__.py
│   │   ├── block.py
│   │   ├── blockchain.py
│   │   └── transaction.py
│   ├── zakat
│   │   ├── __init__.py
│   │   ├── calculator.py
│   │   └── rules.py
│   ├── wallet
│   │   ├── __init__.py
│   │   └── wallet.py
│   ├── mining
│   │   ├── __init__.py
│   │   └── miner.py
│   ├── utils
│   │   ├── __init__.py
│   │   ├── crypto.py
│   │   └── validation.py
│   └── main.py
├── tests
│   ├── __init__.py
│   ├── test_blockchain.py
│   ├── test_zakat.py
│   └── test_wallet.py
├── requirements.txt
