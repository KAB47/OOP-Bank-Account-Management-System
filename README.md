# Bank Account Management System

## Description
The **Bank Account Management System** is a Python program designed to simulate basic bank operations such as transferring funds, depositing money, and withdrawing money. It supports multiple accounts and ensures the validity of operations through account verification and balance checks.

---

## Features
- **Transfer Funds**: Transfer money between valid accounts while ensuring sufficient balance.
- **Deposit Money**: Deposit funds into a valid account.
- **Withdraw Money**: Withdraw funds from an account with sufficient balance.
- **Account Validation**: Ensures that all operations are performed on valid accounts.

---

## Class Overview

### `Bank`
The programme's only class simulates the banking system, managing accounts and transactions.

### Methods

#### `__init__(balance: list[int])`
- Initializes the `Bank` instance with a list of account balances.

#### `is_valid_account(account: int) -> bool`
- Checks if an account number is valid.

#### `transfer(account1: int, account2: int, money: int) -> bool`
- Transfers money between two accounts.
- Returns `True` if successful, `False` otherwise.

#### `deposit(account: int, money: int) -> bool`
- Deposits money into an account.
- Returns `True` if successful, `False` otherwise.

#### `withdraw(account: int, money: int) -> bool`
- Withdraws money from an account.
- Returns `True` if successful, `False` otherwise.

---

## Example Usage

```python
# Create a bank instance
bank = Bank([500, 300, 200]) # 

# Deposit money
print("Deposit:", bank.deposit(1, 100))
print("Balances after deposit:", bank.balance) output: [600, 300, 200]

# Transfer money
print("Transfer:", bank.transfer(1, 2, 50))
print("Balances after transfer:", bank.balance) output: [550, 350, 200]

# Withdraw money
print("Withdraw:", bank.withdraw(3, 100))
print("Balances after withdrawal:", bank.balance) output: [550, 350, 100]

