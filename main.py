class Bank:
    """
    A class representing a bank system that allows deposits, withdrawals,
    and transfers between accounts.
    """

    def __init__(self, balance):
        """
        Initialise the Bank with a list of account balances.

        Args:
            balance (list): A list of integers representing the balance of each account.
        """
        self.balance = balance

    def is_valid_account(self, account):
        """
        Check if the given account number is valid.

        Args:
            account (int): The account number to validate.

        Returns:
            bool: True if the account is valid, False otherwise.
        """
        return 1 <= account <= len(self.balance)

    def transfer(self, account1, account2, money):
        """
        Transfer money from one account to another.

        Args:
            account1 (int): The account number to transfer money from.
            account2 (int): The account number to transfer money to.
            money (int): The amount of money to transfer.

        Returns:
            bool: True if the transfer is successful, False otherwise.
        """
        if not (self.is_valid_account(account1) and self.is_valid_account(account2)):
            return False

        if self.balance[account1 - 1] < money:  # Check sufficient balance
            return False

        self.balance[account1 - 1] -= money
        self.balance[account2 - 1] += money

        return True

    def deposit(self, account, money):
        """
        Deposit money into a specified account.

        Args:
            account (int): The account number to deposit money into.
            money (int): The amount of money to deposit.

        Returns:
            bool: True if the deposit is successful, False otherwise.
        """
        if not self.is_valid_account(account):
            return False

        self.balance[account - 1] += money
        return True

    def withdraw(self, account, money):
        """
        Withdraw money from a specified account.

        Args:
            account (int): The account number to withdraw money from.
            money (int): The amount of money to withdraw.

        Returns:
            bool: True if the withdrawal is successful, False otherwise.
        """
        if not self.is_valid_account(account):
            return False

        if self.balance[account - 1] < money:  # Check sufficient balance
            return False

        self.balance[account - 1] -= money
        return True


# Create a bank instance with initial account balances
bank = Bank([500, 300, 200])

# Deposit money
print("Deposit:", bank.deposit(1, 100))
print("Balances after deposit:", bank.balance)

# Transfer money
print("Transfer:", bank.transfer(1, 2, 50))
print("Balances after transfer:", bank.balance)

# Withdraw money
print("Withdraw:", bank.withdraw(3, 100))
print("Balances after withdrawal:", bank.balance)


