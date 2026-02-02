/**
 * Week 1 - Introduction to OOP in C++
 * First Class Example
 */

#include <iostream>
#include <string>

using namespace std;

// A simple class representing a Student
class Student {
private:
    string name;
    int age;
    string student_id;

public:
    // Constructor
    Student(string n, int a, string id) {
        name = n;
        age = a;
        student_id = id;
    }
    
    // Method to display student information
    void displayInfo() {
        cout << "Name: " << name << endl;
        cout << "Age: " << age << endl;
        cout << "Student ID: " << student_id << endl;
    }
    
    // Method for student to greet
    void greet() {
        cout << "Hello, my name is " << name << "!" << endl;
    }
};

int main() {
    // Creating objects (instances) of the Student class
    Student student1("Alice Johnson", 20, "S001");
    Student student2("Bob Smith", 22, "S002");
    
    // Using object methods
    cout << "Student 1 Information:" << endl;
    student1.displayInfo();
    student1.greet();
    
    cout << "\nStudent 2 Information:" << endl;
    student2.displayInfo();
    student2.greet();
    
    return 0;
}
