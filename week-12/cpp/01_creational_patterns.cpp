/**
 * Week 12 - Creational Design Patterns in C++
 */

#include <iostream>
#include <string>
#include <vector>
#include <memory>

using namespace std;

// 1. Singleton Pattern
class Singleton {
private:
    static Singleton* instance;
    int value;
    
    // Private constructor
    Singleton() : value(0) {}

public:
    // Delete copy constructor and assignment operator
    Singleton(const Singleton&) = delete;
    Singleton& operator=(const Singleton&) = delete;
    
    static Singleton* getInstance() {
        if (instance == nullptr) {
            instance = new Singleton();
        }
        return instance;
    }
    
    void increment() {
        value++;
    }
    
    int getValue() const {
        return value;
    }
};

// Initialize static member
Singleton* Singleton::instance = nullptr;


// 2. Factory Pattern
class Animal {
public:
    virtual string speak() = 0;
    virtual ~Animal() {}
};

class Dog : public Animal {
public:
    string speak() override {
        return "Woof!";
    }
};

class Cat : public Animal {
public:
    string speak() override {
        return "Meow!";
    }
};

class AnimalFactory {
public:
    static unique_ptr<Animal> createAnimal(const string& type) {
        if (type == "dog") {
            return make_unique<Dog>();
        } else if (type == "cat") {
            return make_unique<Cat>();
        }
        return nullptr;
    }
};


// 3. Builder Pattern
class Pizza {
private:
    string size;
    string crust;
    vector<string> toppings;

public:
    void setSize(const string& s) { size = s; }
    void setCrust(const string& c) { crust = c; }
    void addTopping(const string& t) { toppings.push_back(t); }
    
    void display() const {
        cout << size << " pizza with " << crust << " crust and toppings: ";
        for (size_t i = 0; i < toppings.size(); i++) {
            cout << toppings[i];
            if (i < toppings.size() - 1) cout << ", ";
        }
        cout << endl;
    }
};

class PizzaBuilder {
private:
    Pizza pizza;

public:
    PizzaBuilder& setSize(const string& size) {
        pizza.setSize(size);
        return *this;
    }
    
    PizzaBuilder& setCrust(const string& crust) {
        pizza.setCrust(crust);
        return *this;
    }
    
    PizzaBuilder& addTopping(const string& topping) {
        pizza.addTopping(topping);
        return *this;
    }
    
    Pizza build() {
        return pizza;
    }
};


int main() {
    cout << string(60, '=') << endl;
    cout << "Singleton Pattern" << endl;
    cout << string(60, '=') << endl;
    
    Singleton* s1 = Singleton::getInstance();
    Singleton* s2 = Singleton::getInstance();
    
    cout << "s1 == s2: " << (s1 == s2 ? "true" : "false") << endl;
    
    s1->increment();
    cout << "s1 value: " << s1->getValue() << endl;
    cout << "s2 value: " << s2->getValue() << endl;
    
    cout << "\n" << string(60, '=') << endl;
    cout << "Factory Pattern" << endl;
    cout << string(60, '=') << endl;
    
    auto dog = AnimalFactory::createAnimal("dog");
    auto cat = AnimalFactory::createAnimal("cat");
    
    cout << "Dog says: " << dog->speak() << endl;
    cout << "Cat says: " << cat->speak() << endl;
    
    cout << "\n" << string(60, '=') << endl;
    cout << "Builder Pattern" << endl;
    cout << string(60, '=') << endl;
    
    Pizza pizza = PizzaBuilder()
                    .setSize("Large")
                    .setCrust("Thin")
                    .addTopping("Cheese")
                    .addTopping("Pepperoni")
                    .addTopping("Mushrooms")
                    .build();
    
    pizza.display();
    
    return 0;
}
