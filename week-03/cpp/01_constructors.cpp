/**
 * Week 3 - Constructor Types in C++
 */

#include <iostream>
#include <string>
#include <cmath>

using namespace std;

class Point {
private:
    double x, y;

public:
    // Default constructor
    Point() : x(0), y(0) {
        cout << "Default constructor called" << endl;
    }
    
    // Parameterized constructor
    Point(double xVal, double yVal) : x(xVal), y(yVal) {
        cout << "Parameterized constructor called" << endl;
    }
    
    // Copy constructor
    Point(const Point& other) : x(other.x), y(other.y) {
        cout << "Copy constructor called" << endl;
    }
    
    // Destructor
    ~Point() {
        cout << "Destructor called for " << *this << endl;
    }
    
    double distanceTo(const Point& other) const {
        double dx = x - other.x;
        double dy = y - other.y;
        return sqrt(dx*dx + dy*dy);
    }
    
    void display() const {
        cout << "Point(" << x << ", " << y << ")";
    }
    
    friend ostream& operator<<(ostream& os, const Point& p) {
        os << "Point(" << p.x << ", " << p.y << ")";
        return os;
    }
};


class Person {
private:
    string name;
    int age;
    string email;
    string phone;

public:
    // Constructor with default parameters
    Person(string n, int a = 0, string e = "Not provided", string p = "Not provided")
        : name(n), age(a), email(e), phone(p) {
        cout << "Person constructor called for " << name << endl;
    }
    
    // Copy constructor
    Person(const Person& other)
        : name(other.name), age(other.age), email(other.email), phone(other.phone) {
        cout << "Person copy constructor called" << endl;
    }
    
    void display() const {
        cout << "Person('" << name << "', " << age 
             << ", '" << email << "', '" << phone << "')" << endl;
    }
};


int main() {
    cout << string(60, '=') << endl;
    cout << "Point Class - Multiple Constructor Types" << endl;
    cout << string(60, '=') << endl;
    
    Point p1;  // Default constructor
    cout << "p1: " << p1 << endl << endl;
    
    Point p2(3, 4);  // Parameterized constructor
    cout << "p2: " << p2 << endl << endl;
    
    Point p3 = p2;  // Copy constructor
    cout << "p3: " << p3 << endl << endl;
    
    cout << "Distance from p2 to p3: " << p2.distanceTo(p3) << endl;
    
    cout << "\n" << string(60, '=') << endl;
    cout << "Person Class - Constructor with Defaults" << endl;
    cout << string(60, '=') << endl;
    
    Person person1("Alice");
    person1.display();
    cout << endl;
    
    Person person2("Bob", 25);
    person2.display();
    cout << endl;
    
    Person person3("Charlie", 30, "charlie@email.com");
    person3.display();
    cout << endl;
    
    Person person4("Diana", 28, "diana@email.com", "555-1234");
    person4.display();
    cout << endl;
    
    cout << "\nObjects will be destroyed now:" << endl;
    
    return 0;
}
