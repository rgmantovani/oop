#include<string>
#include<iostream>

using namespace std;

class CreateAndDestroy {

    public:
        CreateAndDestroy(int, string); //construtor
        ~CreateAndDestroy();           //destrutor

    private: 
        int objectID;                  //numero de ID do objeto
        string message;                //mensagem descrevendo objeto
};

// construtor
CreateAndDestroy::CreateAndDestroy(int ID, string messageString) {
    objectID = ID;
    message = messageString;

    cout << "Object " << objectID << " constructor runs " << message << endl;
}

CreateAndDestroy::~CreateAndDestroy() {
    cout << "Object " << objectID << " destructor runs " << message << endl;
}


int main(int argc, char* argv[]) {

    cout << "\nMain Function Begins" << endl;
    CreateAndDestroy first(1, "local in main");
    CreateAndDestroy second(2, "local in main");
    CreateAndDestroy third(3, "local in main");
    CreateAndDestroy forth(4, "local in main");
    
    return EXIT_SUCCESS;
}