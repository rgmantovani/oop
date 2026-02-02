"""
Week 10 - Exception Handling in OOP (Python)
"""

# Custom Exception Classes
class InsufficientFundsException(Exception):
    """Raised when withdrawal exceeds balance"""
    
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Insufficient funds: Balance ${balance}, Attempted ${amount}")


class InvalidAccountException(Exception):
    """Raised when account operations are invalid"""
    pass


class BankAccount:
    """Bank account with exception handling"""
    
    def __init__(self, account_number, owner, balance=0):
        if balance < 0:
            raise ValueError("Initial balance cannot be negative")
        
        self.account_number = account_number
        self.owner = owner
        self.balance = balance
        self.is_active = True
    
    def deposit(self, amount):
        """Deposit with validation"""
        if not self.is_active:
            raise InvalidAccountException("Account is closed")
        
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        """Withdraw with exception handling"""
        if not self.is_active:
            raise InvalidAccountException("Account is closed")
        
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        
        if amount > self.balance:
            raise InsufficientFundsException(self.balance, amount)
        
        self.balance -= amount
        return self.balance
    
    def close_account(self):
        """Close the account"""
        if self.balance > 0:
            raise InvalidAccountException(f"Cannot close account with balance ${self.balance}")
        self.is_active = False


class ATM:
    """ATM system with comprehensive error handling"""
    
    def __init__(self):
        self.accounts = {}
    
    def add_account(self, account):
        """Add account to ATM"""
        self.accounts[account.account_number] = account
    
    def process_transaction(self, account_number, transaction_type, amount):
        """Process transaction with error handling"""
        try:
            account = self.accounts[account_number]
            
            if transaction_type == "deposit":
                new_balance = account.deposit(amount)
                print(f"Deposit successful. New balance: ${new_balance}")
            
            elif transaction_type == "withdraw":
                new_balance = account.withdraw(amount)
                print(f"Withdrawal successful. New balance: ${new_balance}")
            
            else:
                raise ValueError(f"Unknown transaction type: {transaction_type}")
        
        except KeyError:
            print(f"Error: Account {account_number} not found")
        
        except InsufficientFundsException as e:
            print(f"Error: {e}")
            print("Transaction declined")
        
        except InvalidAccountException as e:
            print(f"Error: {e}")
        
        except ValueError as e:
            print(f"Error: {e}")
        
        except Exception as e:
            print(f"Unexpected error: {e}")
        
        finally:
            print("Transaction processing complete\n")


if __name__ == "__main__":
    print("=" * 60)
    print("Exception Handling in OOP")
    print("=" * 60)
    
    # Create ATM and accounts
    atm = ATM()
    
    try:
        account1 = BankAccount("ACC001", "Alice", 1000)
        account2 = BankAccount("ACC002", "Bob", 500)
        
        atm.add_account(account1)
        atm.add_account(account2)
        
        # Test successful operations
        print("Test 1: Successful deposit")
        atm.process_transaction("ACC001", "deposit", 500)
        
        print("Test 2: Successful withdrawal")
        atm.process_transaction("ACC001", "withdraw", 200)
        
        print("Test 3: Insufficient funds")
        atm.process_transaction("ACC002", "withdraw", 1000)
        
        print("Test 4: Invalid amount")
        atm.process_transaction("ACC001", "deposit", -100)
        
        print("Test 5: Account not found")
        atm.process_transaction("ACC999", "withdraw", 100)
        
        # Test closing account
        print("Test 6: Closing account with balance")
        try:
            account1.close_account()
        except InvalidAccountException as e:
            print(f"Error: {e}\n")
        
    except Exception as e:
        print(f"Setup error: {e}")
