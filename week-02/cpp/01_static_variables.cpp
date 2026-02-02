/**
 * Week 2 - Instance vs Class (Static) Variables in C++
 */

#include <iostream>
#include <string>

using namespace std;

class Counter {
private:
    string name;
    int count;
    static int totalCount;  // Class variable (static)

public:
    Counter(string n) : name(n), count(0) {
        totalCount++;
    }
    
    void increment() {
        count++;
        totalCount++;
    }
    
    void display() {
        cout << name << ": count = " << count << endl;
        cout << "Total count (class level): " << totalCount << endl;
    }
    
    static int getTotalCount() {
        return totalCount;
    }
};

// Initialize static member
int Counter::totalCount = 0;


class Employee {
private:
    int empId;
    string name;
    double salary;
    static string companyName;  // Class variable
    static int employeeCount;   // Class variable

public:
    Employee(string n, double s) : name(n), salary(s) {
        employeeCount++;
        empId = employeeCount;
    }
    
    void displayInfo() {
        cout << "Employee ID: " << empId << endl;
        cout << "Name: " << name << endl;
        cout << "Salary: $" << salary << endl;
        cout << "Company: " << companyName << endl;
    }
    
    static int getEmployeeCount() {
        return employeeCount;
    }
    
    static void changeCompanyName(string newName) {
        companyName = newName;
    }
    
    static string getCompanyName() {
        return companyName;
    }
};

// Initialize static members
string Employee::companyName = "Tech Corp";
int Employee::employeeCount = 0;


int main() {
    cout << string(60, '=') << endl;
    cout << "Counter Example" << endl;
    cout << string(60, '=') << endl;
    
    Counter counter1("Counter A");
    Counter counter2("Counter B");
    
    cout << "Initial total count: " << Counter::getTotalCount() << endl << endl;
    
    counter1.increment();
    counter1.increment();
    counter1.display();
    cout << endl;
    
    counter2.increment();
    counter2.display();
    cout << endl;
    
    cout << string(60, '=') << endl;
    cout << "Employee Example" << endl;
    cout << string(60, '=') << endl;
    
    Employee emp1("Alice", 75000);
    Employee emp2("Bob", 65000);
    Employee emp3("Charlie", 80000);
    
    emp1.displayInfo();
    cout << endl;
    emp2.displayInfo();
    cout << endl;
    
    cout << "Total employees: " << Employee::getEmployeeCount() << endl;
    
    // Change company name (affects all employees)
    Employee::changeCompanyName("New Tech Corp");
    cout << "\nAfter company name change:" << endl;
    emp3.displayInfo();
    
    return 0;
}
