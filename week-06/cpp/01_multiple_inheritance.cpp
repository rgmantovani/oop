/**
 * Week 6 - Multiple Inheritance in C++
 */

#include <iostream>
#include <string>

using namespace std;

// Example 1: Simple Multiple Inheritance
class Flyable {
public:
    void fly() {
        cout << "Flying in the air" << endl;
    }
};

class Swimmable {
public:
    void swim() {
        cout << "Swimming in water" << endl;
    }
};

class Animal {
protected:
    string name;
public:
    Animal(string n) : name(n) {}
    
    void eat() {
        cout << name << " is eating" << endl;
    }
};

class Duck : public Animal, public Flyable, public Swimmable {
public:
    Duck(string n) : Animal(n) {}
    
    void quack() {
        cout << name << " says: Quack!" << endl;
    }
};


// Example 2: Diamond Problem with Virtual Inheritance
class Base {
public:
    int value;
    Base() : value(0) {
        cout << "Base constructor" << endl;
    }
    
    virtual void display() {
        cout << "Base value: " << value << endl;
    }
};

// Virtual inheritance to solve diamond problem
class Left : virtual public Base {
public:
    Left() {
        cout << "Left constructor" << endl;
    }
};

class Right : virtual public Base {
public:
    Right() {
        cout << "Right constructor" << endl;
    }
};

class Bottom : public Left, public Right {
public:
    Bottom() {
        cout << "Bottom constructor" << endl;
    }
};


int main() {
    cout << string(60, '=') << endl;
    cout << "Multiple Inheritance - Duck Example" << endl;
    cout << string(60, '=') << endl;
    
    Duck duck("Donald");
    duck.eat();   // From Animal
    duck.fly();   // From Flyable
    duck.swim();  // From Swimmable
    duck.quack(); // From Duck
    
    cout << "\n" << string(60, '=') << endl;
    cout << "Diamond Problem with Virtual Inheritance" << endl;
    cout << string(60, '=') << endl;
    
    Bottom b;
    b.value = 42;  // Only one copy of Base due to virtual inheritance
    b.display();
    
    cout << "\nWithout virtual inheritance, there would be ambiguity!" << endl;
    cout << "Virtual inheritance ensures only one Base subobject." << endl;
    
    return 0;
}
