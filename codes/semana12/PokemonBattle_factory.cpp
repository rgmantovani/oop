#include <iostream>
#include <memory>
#include <string>
#include <map>
#include <functional>
#include <stdexcept>
#include <iomanip>
#include <sstream>
#include <vector>

// ── Produto base ──────────────────────────────────────────
// @dataclass ABC  →  classe com construtor explícito
//                    e método puramente virtual (= 0)
class Pokemon {
protected:
    std::string name_;
    int         hp_;
    int         attack_;

public:
    Pokemon(const std::string& name, int hp, int attack)
        : name_(name), hp_(hp), attack_(attack) {}

    // @abstractmethod use_move  →  virtual puro
    virtual void use_move() const = 0;

    // f"{self.name:<14}HP:{self.hp:>4}  ATK:{self.attack:>4}"
    // →  std::setw + std::left / std::right (iomanip)
    std::string status() const {
        std::ostringstream oss;
        oss << std::left  << std::setw(14) << name_
            << "HP:"
            << std::right << std::setw(4)  << hp_
            << "  ATK:"
            << std::right << std::setw(4)  << attack_;
        return oss.str();
    }

    virtual ~Pokemon() = default;
};

// ── Produtos concretos ────────────────────────────────────
class FirePokemon : public Pokemon {
public:
    using Pokemon::Pokemon;   // herda o construtor
    void use_move() const override {
        std::cout << name_ << " usou LANÇA-CHAMAS! "
                  << "(dano base: " << attack_ << ")";
    }
};

class WaterPokemon : public Pokemon {
public:
    using Pokemon::Pokemon;
    void use_move() const override {
        std::cout << name_ << " usou HIDROBOMBA! "
                  << "(dano base: " << attack_ << ")";
    }
};

class GrassPokemon : public Pokemon {
public:
    using Pokemon::Pokemon;
    void use_move() const override {
        std::cout << name_ << " usou FOLHA-NAVALHA! "
                  << "(dano base: " << attack_ << ")";
    }
};

class PsychicPokemon : public Pokemon {
public:
    using Pokemon::Pokemon;
    void use_move() const override {
        std::cout << name_ << " usou PSÍQUICO! "
                  << "(dano base: " << attack_ << ")";
    }
};

// ── Simple Factory com registry ───────────────────────────
// dict[str, type[Pokemon]]
// →  map<string, function<unique_ptr<Pokemon>(string,int,int)>>
//
// Em Python a classe é armazenada e chamada diretamente.
// Em C++ armazenamos uma lambda criadora — mesmo efeito.
class PokemonFactory {
    // Tipo do criador: recebe (name, hp, attack) → unique_ptr
    using Creator = std::function<
        std::unique_ptr<Pokemon>(
            const std::string&, int, int)>;

    // registry estático local (equivale ao atributo de classe)
    static std::map<std::string, Creator>& registry() {
        static std::map<std::string, Creator> reg = {
            {"fire", [](const std::string& n, int hp, int atk){
                return std::make_unique<FirePokemon>(n, hp, atk);
            }},
            {"water", [](const std::string& n, int hp, int atk){
                return std::make_unique<WaterPokemon>(n, hp, atk);
            }},
            {"grass", [](const std::string& n, int hp, int atk){
                return std::make_unique<GrassPokemon>(n, hp, atk);
            }},
            {"psychic", [](const std::string& n, int hp, int atk){
                return std::make_unique<PsychicPokemon>(n, hp, atk);
            }},
        };
        return reg;
    }

public:
    // @classmethod catch  →  static catch_
    // (catch é palavra reservada em C++, usamos catch_)
    static std::unique_ptr<Pokemon>
    catch_(const std::string& poke_type,
           const std::string& name,
           int hp, int attack)
    {
        auto it = registry().find(poke_type);
        if (it == registry().end())
            // raise ValueError  →  throw invalid_argument
            throw std::invalid_argument(
                "Tipo '" + poke_type
                + "' nao existe na Pokedex!");
        return it->second(name, hp, attack);
    }

    // @classmethod register  →  static registerType
    static void registerType(
        const std::string& poke_type, Creator fn)
    {
        registry()[poke_type] = fn;
    }
};

// ── Uso ───────────────────────────────────────────────────
int main() {
    // team_data = [("fire","Charizard",78,84), ...]
    using TeamEntry = std::tuple<
        std::string, std::string, int, int>;

    std::vector<TeamEntry> team_data = {
        {"fire",    "Charizard",  78,  84},
        {"water",   "Blastoise",  79,  83},
        {"grass",   "Venusaur",   80,  82},
        {"psychic", "Mewtwo",    106, 110},
    };

    std::cout << "=== Status do Time ===";
    std::vector<std::unique_ptr<Pokemon>> team;
    for (const auto& [type, name, hp, atk] : team_data) {
        auto p = PokemonFactory::catch_(type, name, hp, atk);
        std::cout << p->status() << "";
        team.push_back(std::move(p));
    }

    std::cout << "=== Batalha! ===";
    for (const auto& p : team)
        p->use_move();

    // Extensão dinâmica — classe local dentro de main()
    // equivale à subclasse inline do Python
    class DragonPokemon : public Pokemon {
    public:
        using Pokemon::Pokemon;
        void use_move() const override {
            std::cout << name_ << " usou PULSO-DRAGÃO! "
                      << "(dano base: " << attack_ << ")";
        }
    };

    PokemonFactory::registerType("dragon",
        [](const std::string& n, int hp, int atk){
            return std::make_unique<DragonPokemon>(n, hp, atk);
        });

    auto dragonite = PokemonFactory::catch_(
        "dragon", "Dragonite", 91, 134);

    std::cout << "=== Novo tipo registrado ===";
    std::cout << dragonite->status() << "";
    dragonite->use_move();

    // try / except ValueError  →  try / catch invalid_argument
    try {
        PokemonFactory::catch_("electric", "Pikachu", 35, 55);
    } catch (const std::invalid_argument& e) {
        std::cout << "Erro: " << e.what() << "";
    }

    return 0;
}