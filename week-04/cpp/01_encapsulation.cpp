/**
 * Week 4 - Encapsulation in C++
 */

#include <iostream>
#include <string>
#include <vector>

using namespace std;

class BankAccount {
private:  // Private members - encapsulated
    string accountNumber;
    string owner;
    double balance;
    vector<string> transactionHistory;

public:
    // Constructor
    BankAccount(string accNum, string own, double initialBalance = 0)
        : accountNumber(accNum), owner(own), balance(initialBalance) {}
    
    // Getter methods
    string getAccountNumber() const {
        return accountNumber;
    }
    
    string getOwner() const {
        return owner;
    }
    
    double getBalance() const {
        return balance;
    }
    
    // Setter with validation
    void setOwner(string newOwner) {
        if (!newOwner.empty()) {
            owner = newOwner;
        } else {
            throw invalid_argument("Owner name cannot be empty");
        }
    }
    
    // Business methods
    bool deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            transactionHistory.push_back("Deposit: +$" + to_string(amount));
            return true;
        }
        return false;
    }
    
    bool withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            transactionHistory.push_back("Withdrawal: -$" + to_string(amount));
            return true;
        }
        return false;
    }
    
    vector<string> getTransactionHistory() const {
        return transactionHistory;
    }
};


class Employee {
private:
    string name;
    double salary;

public:
    Employee(string n, double s) : name(n), salary(s) {}
    
    // Getter for name (read-only)
    string getName() const {
        return name;
    }
    
    // Getter for salary
    double getSalary() const {
        return salary;
    }
    
    // Setter for salary with validation
    void setSalary(double value) {
        if (value < 0) {
            throw invalid_argument("Salary cannot be negative");
        }
        salary = value;
    }
    
    // Computed property
    double getAnnualSalary() const {
        return salary * 12;
    }
    
    void giveRaise(double percentage) {
        if (percentage > 0) {
            salary *= (1 + percentage / 100);
        }
    }
};


int main() {
    cout << string(60, '=') << endl;
    cout << "BankAccount - Encapsulation Example" << endl;
    cout << string(60, '=') << endl;
    
    BankAccount account("ACC001", "John Doe", 1000);
    
    cout << "Account: " << account.getAccountNumber() << endl;
    cout << "Owner: " << account.getOwner() << endl;
    cout << "Balance: $" << account.getBalance() << endl;
    
    account.deposit(500);
    account.withdraw(200);
    
    cout << "\nNew Balance: $" << account.getBalance() << endl;
    cout << "\nTransaction History:" << endl;
    for (const auto& transaction : account.getTransactionHistory()) {
        cout << "  " << transaction << endl;
    }
    
    cout << "\n" << string(60, '=') << endl;
    cout << "Employee - Getters and Setters" << endl;
    cout << string(60, '=') << endl;
    
    Employee emp("Alice", 5000);
    
    cout << "Name: " << emp.getName() << endl;
    cout << "Monthly Salary: $" << emp.getSalary() << endl;
    cout << "Annual Salary: $" << emp.getAnnualSalary() << endl;
    
    emp.giveRaise(10);
    cout << "\nAfter 10% raise:" << endl;
    cout << "Monthly Salary: $" << emp.getSalary() << endl;
    cout << "Annual Salary: $" << emp.getAnnualSalary() << endl;
    
    return 0;
}
