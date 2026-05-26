#include <iostream>
#include <memory>
#include <string>
#include <stdexcept>

// ── Produto base ─────────────────────────────────────────
class Tool {
public:
    virtual std::string getName()       const = 0;
    virtual int         getDurability() const = 0;
    virtual int         getDamage()     const = 0;

    void showInfo() const {
        std::cout << std::left
                  << std::setw(14) << getName()
                  << "dur: " << std::setw(6) << getDurability()
                  << "dmg: " << getDamage() << "\n";
    }

    bool isBroken() const { return getDurability() <= 0; }

    virtual ~Tool() = default;
};

// ── Produtos concretos ───────────────────────────────────
class WoodSword : public Tool {
    int dur;
public:
    WoodSword() : dur(60) {}
    std::string getName()       const override { return "WoodSword"; }
    int         getDurability() const override { return dur; }
    int         getDamage()     const override { return 4; }
    void        use()                          { --dur; }
};

class StoneSword : public Tool {
    int dur;
public:
    StoneSword() : dur(132) {}
    std::string getName()       const override { return "StoneSword"; }
    int         getDurability() const override { return dur; }
    int         getDamage()     const override { return 5; }
    void        use()                          { --dur; }
};

class IronSword : public Tool {
    int dur;
public:
    IronSword() : dur(251) {}
    std::string getName()       const override { return "IronSword"; }
    int         getDurability() const override { return dur; }
    int         getDamage()     const override { return 6; }
    void        use()                          { --dur; }
};

class DiamondSword : public Tool {
    int dur;
public:
    DiamondSword() : dur(1562) {}
    std::string getName()       const override { return "DiamondSword"; }
    int         getDurability() const override { return dur; }
    int         getDamage()     const override { return 7; }
    void        use()                          { --dur; }
};

// ── Simple Factory ───────────────────────────────────────
class ToolFactory {
public:
    static std::unique_ptr<Tool> craft(const std::string& material) {
        if (material == "wood")    return std::make_unique<WoodSword>();
        if (material == "stone")   return std::make_unique<StoneSword>();
        if (material == "iron")    return std::make_unique<IronSword>();
        if (material == "diamond") return std::make_unique<DiamondSword>();
        throw std::invalid_argument(
            "Material desconhecido: " + material);
    }
};

// ── Simulação de combate (Bônus) ─────────────────────────
void simulateCombat(WoodSword& sword) {
    int hits = 0;
    while (!sword.isBroken()) {
        sword.use();
        ++hits;
    }
    std::cout << sword.getName()
              << " quebrou apos " << hits << " golpes!\n";
}

// ── Main ─────────────────────────────────────────────────
#include <iomanip>

int main() {
    std::vector<std::string> materials =
        {"wood", "stone", "iron", "diamond"};

    std::cout << "=== Inventario ===\n";
    for (const auto& m : materials) {
        auto tool = ToolFactory::craft(m);
        tool->showInfo();
    }

    // Bônus: loop de combate
    std::cout << "\n=== Combate ===\n";
    WoodSword ws;
    simulateCombat(ws);

    // Tipo inválido → exceção
    try {
        ToolFactory::craft("gold");
    } catch (const std::invalid_argument& e) {
        std::cout << "Erro: " << e.what() << "\n";
    }

    return 0;
}