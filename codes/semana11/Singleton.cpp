// -------------------------------------------
// -------------------------------------------

#include<string>
#include<iostream>

using namespace std;

// -------------------------------------------
// -------------------------------------------

class Singleton {
    public:
        static Singleton* Instance();
        string getName();
        
    protected:
        Singleton(string);

    private:
        static Singleton* _instance;
        string name;
};

// -------------------------------------------
// -------------------------------------------

Singleton* Singleton::_instance = 0;

// -------------------------------------------
// -------------------------------------------

Singleton::Singleton(string n) {
    name = n;
}

// -------------------------------------------
// -------------------------------------------

Singleton* Singleton::Instance() {
    if(_instance == 0) {
        _instance = new Singleton("unico");
    }
    return (_instance);
}

// -------------------------------------------
// -------------------------------------------

string Singleton::getName() {
    return(name);
}

// -------------------------------------------
// -------------------------------------------

int main(int argc, char* argv[]) {

    Singleton* a = Singleton::Instance();
    Singleton* b = Singleton::Instance();

    cout << "nome de A: " << a->getName() << endl;
    cout << "nome de B: " << b->getName() << endl;
}

// -------------------------------------------
// -------------------------------------------