/**
 * Week 1 - Exercise Solutions (C++)
 */

#include <iostream>
#include <string>
#include <ctime>

using namespace std;

// Exercise 1: Car Class
class Car {
private:
    string brand;
    string model;
    int year;
    string color;

public:
    Car(string b, string m, int y, string c) 
        : brand(b), model(m), year(y), color(c) {}
    
    void displayInfo() {
        cout << "Brand: " << brand << endl;
        cout << "Model: " << model << endl;
        cout << "Year: " << year << endl;
        cout << "Color: " << color << endl;
    }
    
    int age() {
        time_t now = time(0);
        tm* ltm = localtime(&now);
        int currentYear = 1900 + ltm->tm_year;
        return currentYear - year;
    }
};

// Exercise 2: Rectangle Class
class Rectangle {
private:
    double width;
    double height;

public:
    Rectangle(double w, double h) : width(w), height(h) {}
    
    double area() {
        return width * height;
    }
    
    double perimeter() {
        return 2 * (width + height);
    }
    
    bool isSquare() {
        return width == height;
    }
    
    double getWidth() { return width; }
    double getHeight() { return height; }
};

// Exercise 3: BankAccount Class
class BankAccount {
private:
    string accountNumber;
    string ownerName;
    double balance;

public:
    BankAccount(string accNum, string name, double bal = 0.0)
        : accountNumber(accNum), ownerName(name), balance(bal) {}
    
    void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            cout << "Deposited $" << amount << ". New balance: $" << balance << endl;
        } else {
            cout << "Invalid deposit amount!" << endl;
        }
    }
    
    void withdraw(double amount) {
        if (amount > balance) {
            cout << "Insufficient funds! Current balance: $" << balance << endl;
        } else if (amount <= 0) {
            cout << "Invalid withdrawal amount!" << endl;
        } else {
            balance -= amount;
            cout << "Withdrew $" << amount << ". New balance: $" << balance << endl;
        }
    }
    
    void displayBalance() {
        cout << "Account " << accountNumber << " - " << ownerName << endl;
        cout << "Current Balance: $" << balance << endl;
    }
};

int main() {
    cout << string(60, '=') << endl;
    cout << "Exercise 1: Car Class" << endl;
    cout << string(60, '=') << endl;
    
    Car car1("Toyota", "Camry", 2020, "Silver");
    Car car2("Honda", "Civic", 2018, "Blue");
    Car car3("Ford", "Mustang", 2022, "Red");
    
    car1.displayInfo();
    cout << "Age: " << car1.age() << " years\n" << endl;
    
    car2.displayInfo();
    cout << "Age: " << car2.age() << " years\n" << endl;
    
    car3.displayInfo();
    cout << "Age: " << car3.age() << " years\n" << endl;
    
    cout << string(60, '=') << endl;
    cout << "Exercise 2: Rectangle Class" << endl;
    cout << string(60, '=') << endl;
    
    Rectangle rect1(5, 10);
    Rectangle rect2(7, 7);
    Rectangle rect3(3.5, 8.2);
    
    cout << "Rectangle 1: " << rect1.getWidth() << " x " << rect1.getHeight() << endl;
    cout << "Area: " << rect1.area() << ", Perimeter: " << rect1.perimeter() << endl;
    cout << "Is square? " << (rect1.isSquare() ? "Yes" : "No") << "\n" << endl;
    
    cout << "Rectangle 2: " << rect2.getWidth() << " x " << rect2.getHeight() << endl;
    cout << "Area: " << rect2.area() << ", Perimeter: " << rect2.perimeter() << endl;
    cout << "Is square? " << (rect2.isSquare() ? "Yes" : "No") << "\n" << endl;
    
    cout << "Rectangle 3: " << rect3.getWidth() << " x " << rect3.getHeight() << endl;
    cout << "Area: " << rect3.area() << ", Perimeter: " << rect3.perimeter() << endl;
    cout << "Is square? " << (rect3.isSquare() ? "Yes" : "No") << "\n" << endl;
    
    cout << string(60, '=') << endl;
    cout << "Exercise 3: BankAccount Class" << endl;
    cout << string(60, '=') << endl;
    
    BankAccount account("ACC001", "John Doe", 1000.0);
    account.displayBalance();
    cout << endl;
    
    account.deposit(500.0);
    account.withdraw(200.0);
    account.withdraw(2000.0);  // Should fail
    cout << endl;
    account.displayBalance();
    
    return 0;
}
