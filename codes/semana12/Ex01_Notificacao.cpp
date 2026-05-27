#include <iostream>
#include <memory>

using namespace std;

// Produto abstrato
class Notificacao {
public:
    virtual void enviar(string mensagem) = 0;
    virtual ~Notificacao() {}
};

// Produtos concretos
class Email : public Notificacao {
public:
    void enviar(string mensagem) override {
        cout << "[EMAIL] " << mensagem << endl;
    }
};

class SMS : public Notificacao {
public:
    void enviar(string mensagem) override {
        cout << "[SMS] " << mensagem << endl;
    }
};

class Push : public Notificacao {
public:
    void enviar(string mensagem) override {
        cout << "[PUSH] " << mensagem << endl;
    }
};

// Factory
class FabricaNotificacao {
public:

    static unique_ptr<Notificacao> criar(string tipo) {

        if (tipo == "email")
            return make_unique<Email>();

        else if (tipo == "sms")
            return make_unique<SMS>();

        else if (tipo == "push")
            return make_unique<Push>();

        return nullptr;
    }
};

int main() {

    string tipo;

    cout << "Digite o tipo (email/sms/push): ";
    cin >> tipo;

    auto notificacao = FabricaNotificacao::criar(tipo);

    if (notificacao)
        notificacao->enviar("Bem-vindo ao sistema!");
    else
        cout << "Tipo invalido!" << endl;

    return 0;
}