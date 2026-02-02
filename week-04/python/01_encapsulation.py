"""
Week 4 - Encapsulation in Python
"""

class BankAccount:
    """Bank account demonstrating encapsulation"""
    
    def __init__(self, account_number, owner, initial_balance=0):
        self.__account_number = account_number  # Private
        self.__owner = owner  # Private
        self.__balance = initial_balance  # Private
        self.__transaction_history = []  # Private
    
    # Getter methods
    def get_account_number(self):
        """Get account number (read-only)"""
        return self.__account_number
    
    def get_owner(self):
        """Get owner name"""
        return self.__owner
    
    def get_balance(self):
        """Get current balance"""
        return self.__balance
    
    # Setter with validation
    def set_owner(self, new_owner):
        """Set owner name with validation"""
        if new_owner and len(new_owner) > 0:
            self.__owner = new_owner
        else:
            raise ValueError("Owner name cannot be empty")
    
    # Business methods
    def deposit(self, amount):
        """Deposit money"""
        if amount > 0:
            self.__balance += amount
            self.__transaction_history.append(f"Deposit: +${amount}")
            return True
        return False
    
    def withdraw(self, amount):
        """Withdraw money"""
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            self.__transaction_history.append(f"Withdrawal: -${amount}")
            return True
        return False
    
    def get_transaction_history(self):
        """Get copy of transaction history"""
        return self.__transaction_history.copy()


class Employee:
    """Employee class with property decorators"""
    
    def __init__(self, name, salary):
        self._name = name
        self._salary = salary
    
    @property
    def name(self):
        """Name property (read-only)"""
        return self._name
    
    @property
    def salary(self):
        """Salary property"""
        return self._salary
    
    @salary.setter
    def salary(self, value):
        """Salary setter with validation"""
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._salary = value
    
    @property
    def annual_salary(self):
        """Computed property"""
        return self._salary * 12
    
    def give_raise(self, percentage):
        """Give percentage raise"""
        if percentage > 0:
            self._salary *= (1 + percentage / 100)


if __name__ == "__main__":
    print("=" * 60)
    print("BankAccount - Encapsulation Example")
    print("=" * 60)
    
    account = BankAccount("ACC001", "John Doe", 1000)
    
    print(f"Account: {account.get_account_number()}")
    print(f"Owner: {account.get_owner()}")
    print(f"Balance: ${account.get_balance()}")
    
    account.deposit(500)
    account.withdraw(200)
    
    print(f"\nNew Balance: ${account.get_balance()}")
    print("\nTransaction History:")
    for transaction in account.get_transaction_history():
        print(f"  {transaction}")
    
    # Cannot directly access private attributes
    # print(account.__balance)  # This would raise AttributeError
    
    print("\n" + "=" * 60)
    print("Employee - Property Decorators")
    print("=" * 60)
    
    emp = Employee("Alice", 5000)
    
    print(f"Name: {emp.name}")
    print(f"Monthly Salary: ${emp.salary}")
    print(f"Annual Salary: ${emp.annual_salary}")
    
    emp.give_raise(10)
    print(f"\nAfter 10% raise:")
    print(f"Monthly Salary: ${emp.salary}")
    print(f"Annual Salary: ${emp.annual_salary}")
