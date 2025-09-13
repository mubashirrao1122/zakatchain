Zakat Blockchain Simulation

Overview

This is a simple, educational blockchain simulation focused on Zakat (2.5% charitable deduction). It uses only core Python data structures (lists and dictionaries) and a minimal Block/Blockchain model. A student roll number is incorporated into block hashing to personalize the chain.

Key points
- Wallets start with a default balance of 200 units and keep a small transaction log.
- Zakat is calculated at 2.5% of the current wallet balance and deducted before each transfer in the demo.
- Blocks store lists of transaction dictionaries and link to the previous block via a SHA-256 hash.
- The block hash is seeded with the student roll number for uniqueness.
- No Proof-of-Work, networking, or consensus is implemented; this is a local, single-node simulation.

Architecture at a glance
- Wallet (`src/wallet/wallet.py`)
	- balance: float (default 200.0)
	- transactions: list[dict]
	- add_funds(amount), deduct_zakat(), calculate_zakat(), update_balance(delta), get_balance()
- Block (`src/blockchain/block.py`)
	- index: int, transactions: list[dict], previous_hash: str, timestamp: int, roll_number: str|int, hash: str
	- Hashing: sha256( str(roll_number) || f"{index}{timestamp}{transactions}{previous_hash}{roll_number}" )
- Blockchain (`src/blockchain/blockchain.py`)
	- chain: list[Block], current_transactions: list[dict], roll_number
	- create_genesis_block(), add_transaction(...), new_block(transactions), last_block, validate_chain()
- Zakat utilities
	- `src/zakat/calculator.py`: calculate_zakat(balance), record_deduction(balance)
	- `src/zakat/rules.py`: ZakatRules with is_eligible_for_zakat(), calculate_zakat(), log_transaction()
- Transaction model (`src/blockchain/transaction.py`)
	- Lightweight container with to_dict(); the simulation uses plain dicts directly.

How it works
1) Set your roll number in `src/main.py`.
2) Two wallets (Mubashir and Saim) are created with default balances.
3) For each demo transfer:
	 - Sender’s Zakat (2.5% of current balance) is deducted: sender.deduct_zakat().
	 - Balances are updated: sender.update_balance(-amount), receiver.update_balance(+amount).
	 - A transaction dict is appended to the blockchain’s `current_transactions`.
4) After processing the demo list, a new block is created with `new_block(current_transactions)`, linked to the previous block via previous_hash and hashed with the roll-number seed.
5) The chain is printed: Block index, hash, and transactions.

Project structure
```
README.md
requirements.txt
setup.py
src/
	main.py
	blockchain/
		__init__.py
		block.py
		blockchain.py
		transaction.py
	mining/
		__init__.py
		miner.py              # legacy/unused in current flow
	utils/
		__init__.py
		crypto.py             # legacy helpers (hash_data)
		validation.py         # legacy validation helpers
	wallet/
		__init__.py
		wallet.py
	zakat/
		__init__.py
		calculator.py
		rules.py
tests/
	__init__.py
	test_blockchain.py
	test_wallet.py
	test_zakat.py
```

Quickstart
Prerequisites: Python 3.10+ recommended.

1) (Optional) Create and activate a virtual environment.
2) Install dependencies: pip install -r requirements.txt
	 - Note: Only pytest is used at runtime for tests; Flask/requests/cryptography are present but not required for the core demo.
3) Run the simulation: python src/main.py
	 - Edit `roll_number` in `src/main.py` to personalize the chain.

Running tests
- From the project root, run: pytest
- Tests target modules under `src/` using absolute imports like `from src.zakat...`.

Notes about tests vs current APIs
- Zakat tests (tests/test_zakat.py) align with the current code and should pass.
- Wallet tests expect Wallet(initial_balance=...) and some overdraft behavior not present in the current Wallet implementation (which starts at 200.0 and doesn’t guard against negative balances). If you want to satisfy those tests, consider:
	- Updating Wallet.__init__ to accept optional initial_balance and set balance accordingly.
	- Guarding update_balance to prevent dropping below zero (or adjust expected behavior).
- Blockchain tests assume different constructor and method signatures (e.g., `Blockchain()` without a roll number, different Block/Transaction init shapes). The current implementation requires `Blockchain(roll_number)` and uses dict transactions. To satisfy those tests you could:
	- Provide default roll_number in Blockchain.__init__ (e.g., a fixed fallback) and add adapter methods (`add_block`) if needed.
	- Or update the tests to use `add_transaction(...)` + `new_block(...)` and the existing Block signature.

API reference (essentials)
- Wallet
	- Wallet(): balance=200.0 by default
	- deduct_zakat() -> float: deducts 2.5% of current balance and returns the deducted amount
	- update_balance(amount: float) -> bool: adds amount (can be negative)
	- get_balance() -> float
	- calculate_zakat() -> float
- Blockchain
	- Blockchain(roll_number)
	- add_transaction(sender, receiver, zakat_deducted, remaining_balance) -> int (next block index)
	- new_block(transactions: list[dict]) -> Block
	- validate_chain() -> bool
	- last_block (property) -> Block
- Block
	- Fields: index, transactions, previous_hash, timestamp, roll_number, hash

Design choices and limitations
- Educational focus: no Proof-of-Work, no P2P networking, no mempool rules, no digital signatures.
- Transaction objects are plain dictionaries to keep things simple.
- Hashing includes the roll number to make each student’s chain unique.

Troubleshooting
- Import errors when running tests: run `pytest` from the project root so `src` is importable (`from src...`).
- If you see failed wallet/blockchain tests, review the “Notes about tests vs current APIs” and align either code or tests.
- If running on a clean environment, ensure Python 3.10+ and dependencies are installed.

License
- Educational sample; no explicit license provided.


