#include <iostream>
#include <memory>

using namespace std;

// Produto abstrato
class Transporte {
public:
    virtual void viajar() = 0;
    virtual ~Transporte() {}
};

// Produtos concretos
class Onibus : public Transporte {
public:
    void viajar() override {
        cout << "Ônibus realizando rota urbana." << endl;
    }
};

class Taxi : public Transporte {
public:
    void viajar() override {
        cout << "Táxi transportando passageiro." << endl;
    }
};

class Bicicleta : public Transporte {
public:
    void viajar() override {
        cout << "Bicicleta compartilhada iniciando trajeto." << endl;
    }
};

// Factory
class FabricaTransporte {
public:

    static unique_ptr<Transporte> criar(string tipo) {

        if (tipo == "onibus")
            return make_unique<Onibus>();

        else if (tipo == "taxi")
            return make_unique<Taxi>();

        else if (tipo == "bicicleta")
            return make_unique<Bicicleta>();

        return nullptr;
    }
};

int main() {

    string tipo;

    cout << "Escolha o transporte: ";
    cin >> tipo;

    auto transporte = FabricaTransporte::criar(tipo);

    if (transporte)
        transporte->viajar();
    else
        cout << "Tipo de transporte invalido!" << endl;

    return 0;
}