/**
 * Week 2 - Constructors and Destructors in C++
 */

#include <iostream>
#include <string>
#include <cmath>

using namespace std;

class Resource {
private:
    string name;
    int size;
    static int resourceCount;

public:
    // Constructor
    Resource(string n, int s) : name(n), size(s) {
        resourceCount++;
        cout << "Resource '" << name << "' created (size: " << size << " MB)" << endl;
        cout << "Total resources: " << resourceCount << endl;
    }
    
    // Destructor
    ~Resource() {
        resourceCount--;
        cout << "Resource '" << name << "' destroyed" << endl;
        cout << "Remaining resources: " << resourceCount << endl;
    }
    
    static int getResourceCount() {
        return resourceCount;
    }
};

int Resource::resourceCount = 0;


class Point {
private:
    double x, y;

public:
    // Default constructor
    Point() : x(0), y(0) {
        cout << "Point created at (" << x << ", " << y << ")" << endl;
    }
    
    // Parameterized constructor
    Point(double xVal, double yVal) : x(xVal), y(yVal) {
        cout << "Point created at (" << x << ", " << y << ")" << endl;
    }
    
    // Copy constructor
    Point(const Point& other) : x(other.x), y(other.y) {
        cout << "Point copied to (" << x << ", " << y << ")" << endl;
    }
    
    double distanceFromOrigin() {
        return sqrt(x * x + y * y);
    }
    
    void display() {
        cout << "Point(" << x << ", " << y << ")";
    }
};


class BankAccount {
private:
    string accountNumber;
    string ownerName;
    double balance;
    string accountType;

public:
    // Constructor with default parameters
    BankAccount(string accNum, string owner, double bal = 0.0, string type = "Savings")
        : accountNumber(accNum), ownerName(owner), balance(bal), accountType(type) {
        cout << "Account created: " << accountNumber << " - " << ownerName << endl;
    }
    
    void display() {
        cout << "BankAccount('" << accountNumber << "', '" << ownerName 
             << "', " << balance << ", '" << accountType << "')" << endl;
    }
};


int main() {
    cout << string(60, '=') << endl;
    cout << "Resource Management Example" << endl;
    cout << string(60, '=') << endl;
    
    {
        Resource res1("Image1", 5);
        Resource res2("Video1", 100);
        cout << endl;
        
        // res1 and res2 will be destroyed at end of this block
    }
    
    cout << "\nAfter block - resources destroyed" << endl;
    
    Resource res3("Audio1", 3);
    cout << "\nEnd of program - remaining objects will be destroyed\n" << endl;
    
    cout << string(60, '=') << endl;
    cout << "Point Example" << endl;
    cout << string(60, '=') << endl;
    
    Point p1;  // Default constructor
    Point p2(3, 4);  // Parameterized constructor
    Point p3 = p2;  // Copy constructor
    
    cout << "\np1: ";
    p1.display();
    cout << ", Distance: " << p1.distanceFromOrigin() << endl;
    
    cout << "p2: ";
    p2.display();
    cout << ", Distance: " << p2.distanceFromOrigin() << endl;
    
    cout << "\n" << string(60, '=') << endl;
    cout << "BankAccount Example" << endl;
    cout << string(60, '=') << endl;
    
    // Different ways to create objects
    BankAccount acc1("ACC001", "John Doe");
    BankAccount acc2("ACC002", "Jane Smith", 1000.0);
    BankAccount acc3("ACC003", "Bob Johnson", 5000.0, "Checking");
    
    cout << endl;
    acc1.display();
    acc2.display();
    acc3.display();
    
    return 0;
}
