
#include <iostream>
#include <vector>
#include <string>

// ── Singleton ────────────────────────────────────────────

class Logger {

    private: 
        std::vector<std::string> mensagens_;
        Logger() = default;

    public:
        Logger(const Logger&)            = delete;
        Logger& operator=(const Logger&) = delete;

        static Logger& instancia() {
            static Logger inst;
            return inst;
        }

        void registrar(const std::string& msg) {
            mensagens_.push_back(msg);
            std::cout << "[LOG #" << mensagens_.size() << "] " << msg << "\n";
        }

        void exibir_todos() const {
            std::cout << "\nTotal de eventos: " << mensagens_.size() << "\n";
        }
};

// ── Classes consumidoras ─────────────────────────────────
class Heroi {

    private:
        std::string nome_;

    public:
        explicit Heroi(std::string nome) : nome_(std::move(nome)) { }

        void atacar(const std::string& alvo, const std::string& arma) {
            Logger::instancia().registrar(nome_ + " atacou " + alvo + " com " + arma);
        }

        void usar_magia(const std::string& magia, const std::string& alvo) {
            Logger::instancia().registrar(nome_ + " usou " + magia + " em " + alvo);
        }
};

class Inimigo {
    
    private:
        std::string nome_;
    
    public:
        explicit Inimigo(std::string nome) : nome_(std::move(nome)) {}

        void receber_dano(int qtd) {
            Logger::instancia().registrar(nome_ + " recebeu " + std::to_string(qtd) + " de dano");
        }
};

// ── Main ─────────────────────────────────────────────────
int main() {

    Heroi  heroi("Herói");
    Inimigo dragao("Dragão");

    heroi.atacar("Dragão", "espada");
    dragao.receber_dano(40);
    heroi.usar_magia("Bola de Fogo", "Dragão");
    dragao.receber_dano(80);

    Logger::instancia().exibir_todos();

    // Prova: mesmo endereço
    auto& a = Logger::instancia();
    auto& b = Logger::instancia();
    std::cout << "Mesma instância? " << (&a == &b ? "True ✓" : "False ✗") << "\n";
    return 0;
}
