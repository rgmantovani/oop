/**
 * Week 1 - Comparing Procedural and OOP approaches in C++
 */

#include <iostream>
#include <string>

using namespace std;

// PROCEDURAL APPROACH - Function to display book
void displayBook(string title, string author, int pages) {
    cout << "Title: " << title << endl;
    cout << "Author: " << author << endl;
    cout << "Pages: " << pages << endl;
}

// OOP APPROACH - Book class
class Book {
private:
    string title;
    string author;
    int pages;

public:
    // Constructor
    Book(string t, string a, int p) : title(t), author(a), pages(p) {}
    
    // Method to display book information
    void displayInfo() {
        cout << "Title: " << title << endl;
        cout << "Author: " << author << endl;
        cout << "Pages: " << pages << endl;
    }
    
    // Method to check if book is long
    bool isLongBook() {
        return pages > 400;
    }
};

int main() {
    cout << string(50, '=') << endl;
    cout << "PROCEDURAL APPROACH" << endl;
    cout << string(50, '=') << endl;
    
    // Data stored in separate variables
    string book1_title = "Python Programming";
    string book1_author = "John Doe";
    int book1_pages = 350;
    
    string book2_title = "C++ Fundamentals";
    string book2_author = "Jane Smith";
    int book2_pages = 420;
    
    displayBook(book1_title, book1_author, book1_pages);
    cout << endl;
    displayBook(book2_title, book2_author, book2_pages);
    
    cout << "\n" << string(50, '=') << endl;
    cout << "OBJECT-ORIENTED APPROACH" << endl;
    cout << string(50, '=') << endl;
    
    // Creating objects
    Book book1("Python Programming", "John Doe", 350);
    Book book2("C++ Fundamentals", "Jane Smith", 420);
    
    // Using objects
    book1.displayInfo();
    cout << "Is long book? " << (book1.isLongBook() ? "Yes" : "No") << endl;
    cout << endl;
    
    book2.displayInfo();
    cout << "Is long book? " << (book2.isLongBook() ? "Yes" : "No") << endl;
    
    cout << "\n" << string(50, '=') << endl;
    cout << "ADVANTAGES OF OOP:" << endl;
    cout << "- Data and methods bundled together" << endl;
    cout << "- Better organization and reusability" << endl;
    cout << "- Easier to maintain and extend" << endl;
    cout << "- Models real-world entities naturally" << endl;
    
    return 0;
}
