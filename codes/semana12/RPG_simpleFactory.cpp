#include <iostream>
#include <memory>
#include <string>
#include <map>
#include <functional>
#include <stdexcept>

// ── Produto base ──────────────────────────────────────────
class RPGCharacter {
public:
    virtual std::string className() const = 0;
    virtual void showStats() const = 0;
    virtual ~RPGCharacter() = default;
};

// ── Produtos concretos ────────────────────────────────────
class Knight : public RPGCharacter {
public:
    std::string className() const override { return "Cavaleiro"; }
    void showStats() const override {
        std::cout << "[Cavaleiro]  HP: 200  ATK:  80  DEF: 120\n";
    }
};

class Mage : public RPGCharacter {
public:
    std::string className() const override { return "Mago"; }
    void showStats() const override {
        std::cout << "[Mago]       HP: 100  ATK: 150  DEF:  40\n";
    }
};

class Rogue : public RPGCharacter {
public:
    std::string className() const override { return "Ladino"; }
    void showStats() const override {
        std::cout << "[Ladino]     HP: 130  ATK: 110  DEF:  70\n";
    }
};

// ── Simple Factory ────────────────────────────────────────
// Usa um mapa de fábrica para evitar if/else crescente
// e facilitar extensão (OCP).
class CharacterFactory {
    using Creator = std::function<std::unique_ptr<RPGCharacter>()>;

    static std::map<std::string, Creator>& registry() {
        static std::map<std::string, Creator> reg = {
            {"knight", []{ return std::make_unique<Knight>(); }},
            {"mage",   []{ return std::make_unique<Mage>();   }},
            {"rogue",  []{ return std::make_unique<Rogue>();  }},
        };
        return reg;
    }

public:
    static std::unique_ptr<RPGCharacter>
    create(const std::string& cls) {
        auto it = registry().find(cls);
        if (it == registry().end())
            throw std::invalid_argument(
                "Classe desconhecida: " + cls);
        return it->second();
    }

    // Registro dinâmico — Open/Closed Principle
    static void registerClass(const std::string& key, Creator fn) {
        registry()[key] = fn;
    }
};

// ── Main ──────────────────────────────────────────────────
int main() {
    std::cout << "=== Selecione sua classe ===\n";
    for (const auto& cls : {"knight", "mage", "rogue"}) {
        auto hero = CharacterFactory::create(cls);
        hero->showStats();
    }

    // Extensão dinâmica sem alterar o código acima
    class Paladin : public RPGCharacter {
    public:
        std::string className() const override { return "Paladino"; }
        void showStats() const override {
            std::cout << "[Paladino]   HP: 180  ATK:  90  DEF: 110\n";
        }
    };
    CharacterFactory::registerClass("paladin",
        []{ return std::make_unique<Paladin>(); });

    std::cout << "\n=== Nova classe desbloqueada ===\n";
    CharacterFactory::create("paladin")->showStats();

    // Classe inválida
    try {
        CharacterFactory::create("wizard");
    } catch (const std::invalid_argument& e) {
        std::cout << "Erro: " << e.what() << "\n";
    }
    return 0;
}