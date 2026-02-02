/**
 * Week 8 - Abstract Classes in C++
 */

#include <iostream>
#include <string>
#include <cmath>

using namespace std;

// Example 1: Shape hierarchy with abstract base class
class Shape {
public:
    // Pure virtual functions (abstract methods)
    virtual double area() = 0;
    virtual double perimeter() = 0;
    
    // Concrete method
    virtual string description() {
        return "This is a Shape";
    }
    
    // Virtual destructor for proper cleanup
    virtual ~Shape() {}
};

class Rectangle : public Shape {
private:
    double width, height;

public:
    Rectangle(double w, double h) : width(w), height(h) {}
    
    double area() override {
        return width * height;
    }
    
    double perimeter() override {
        return 2 * (width + height);
    }
    
    string description() override {
        return "This is a Rectangle";
    }
};

class Circle : public Shape {
private:
    double radius;

public:
    Circle(double r) : radius(r) {}
    
    double area() override {
        return M_PI * radius * radius;
    }
    
    double perimeter() override {
        return 2 * M_PI * radius;
    }
    
    string description() override {
        return "This is a Circle";
    }
};


// Example 2: Payment system with interface-like abstract class
class PaymentMethod {
public:
    // Pure virtual functions
    virtual bool processPayment(double amount) = 0;
    virtual bool refund(double amount) = 0;
    
    virtual ~PaymentMethod() {}
};

class CreditCard : public PaymentMethod {
private:
    string cardNumber;

public:
    CreditCard(string number) : cardNumber(number) {}
    
    bool processPayment(double amount) override {
        cout << "Processing $" << amount << " payment with Credit Card ending in " 
             << cardNumber.substr(cardNumber.length() - 4) << endl;
        return true;
    }
    
    bool refund(double amount) override {
        cout << "Refunding $" << amount << " to Credit Card ending in " 
             << cardNumber.substr(cardNumber.length() - 4) << endl;
        return true;
    }
};

class PayPal : public PaymentMethod {
private:
    string email;

public:
    PayPal(string e) : email(e) {}
    
    bool processPayment(double amount) override {
        cout << "Processing $" << amount << " payment via PayPal account " << email << endl;
        return true;
    }
    
    bool refund(double amount) override {
        cout << "Refunding $" << amount << " to PayPal account " << email << endl;
        return true;
    }
};


int main() {
    cout << string(60, '=') << endl;
    cout << "Abstract Classes - Shape Hierarchy" << endl;
    cout << string(60, '=') << endl;
    
    // Cannot instantiate abstract class
    // Shape* shape = new Shape();  // This would cause compilation error
    
    Shape* rect = new Rectangle(5, 10);
    cout << rect->description() << endl;
    cout << "Area: " << rect->area() << endl;
    cout << "Perimeter: " << rect->perimeter() << endl;
    
    cout << endl;
    
    Shape* circle = new Circle(7);
    cout << circle->description() << endl;
    cout << "Area: " << circle->area() << endl;
    cout << "Perimeter: " << circle->perimeter() << endl;
    
    delete rect;
    delete circle;
    
    cout << "\n" << string(60, '=') << endl;
    cout << "Abstract Classes - Payment System" << endl;
    cout << string(60, '=') << endl;
    
    PaymentMethod* payment1 = new CreditCard("1234567890123456");
    payment1->processPayment(100.50);
    payment1->refund(25.00);
    
    cout << endl;
    
    PaymentMethod* payment2 = new PayPal("user@example.com");
    payment2->processPayment(75.25);
    payment2->refund(10.00);
    
    delete payment1;
    delete payment2;
    
    return 0;
}
