/**
 * Week 5 - Single Inheritance in C++
 */

#include <iostream>
#include <string>

using namespace std;

// Base class
class Animal {
protected:
    string name;
    int age;

public:
    Animal(string n, int a) : name(n), age(a) {}
    
    void eat() {
        cout << name << " is eating" << endl;
    }
    
    void sleep() {
        cout << name << " is sleeping" << endl;
    }
    
    virtual void makeSound() {
        cout << name << " makes a sound" << endl;
    }
    
    string getName() const { return name; }
    int getAge() const { return age; }
};

// Derived class
class Dog : public Animal {
private:
    string breed;

public:
    Dog(string n, int a, string b) : Animal(n, a), breed(b) {}
    
    void makeSound() override {
        cout << name << " barks: Woof! Woof!" << endl;
    }
    
    void fetch() {
        cout << name << " is fetching the ball" << endl;
    }
    
    string getBreed() const { return breed; }
};

class Cat : public Animal {
private:
    string color;

public:
    Cat(string n, int a, string c) : Animal(n, a), color(c) {}
    
    void makeSound() override {
        cout << name << " meows: Meow!" << endl;
    }
    
    void climb() {
        cout << name << " is climbing a tree" << endl;
    }
    
    string getColor() const { return color; }
};


class Vehicle {
protected:
    string brand;
    string model;
    int year;

public:
    Vehicle(string b, string m, int y) : brand(b), model(m), year(y) {}
    
    void start() {
        cout << brand << " " << model << " is starting" << endl;
    }
    
    void stop() {
        cout << brand << " " << model << " is stopping" << endl;
    }
    
    string getBrand() const { return brand; }
    string getModel() const { return model; }
    int getYear() const { return year; }
};

class Car : public Vehicle {
private:
    int numDoors;

public:
    Car(string b, string m, int y, int doors) 
        : Vehicle(b, m, y), numDoors(doors) {}
    
    void honk() {
        cout << "Beep beep!" << endl;
    }
    
    int getNumDoors() const { return numDoors; }
};


int main() {
    cout << string(60, '=') << endl;
    cout << "Animal Hierarchy" << endl;
    cout << string(60, '=') << endl;
    
    // Create Dog object
    Dog dog("Buddy", 3, "Golden Retriever");
    cout << "Name: " << dog.getName() << ", Age: " << dog.getAge() 
         << ", Breed: " << dog.getBreed() << endl;
    dog.eat();  // Inherited method
    dog.sleep();  // Inherited method
    dog.makeSound();  // Overridden method
    dog.fetch();  // Dog-specific method
    
    cout << "\n" << string(60, '=') << endl;
    
    // Create Cat object
    Cat cat("Whiskers", 2, "Orange");
    cout << "Name: " << cat.getName() << ", Age: " << cat.getAge() 
         << ", Color: " << cat.getColor() << endl;
    cat.eat();  // Inherited method
    cat.makeSound();  // Overridden method
    cat.climb();  // Cat-specific method
    
    cout << "\n" << string(60, '=') << endl;
    cout << "Vehicle Hierarchy" << endl;
    cout << string(60, '=') << endl;
    
    Car car("Toyota", "Camry", 2022, 4);
    cout << car.getBrand() << " " << car.getModel() << " (" << car.getYear() 
         << ") - " << car.getNumDoors() << " doors" << endl;
    car.start();  // Inherited method
    car.honk();  // Car-specific method
    car.stop();  // Inherited method
    
    return 0;
}
