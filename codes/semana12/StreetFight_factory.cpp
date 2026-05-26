#include <iostream>
#include <memory>
#include <string>
#include <vector>

// ── Produto: Golpe Especial ───────────────────────────────
class SpecialMove {
public:
    virtual void execute(const std::string& fighter) const = 0;
    virtual std::string moveName() const = 0;
    virtual ~SpecialMove() = default;
};

class Hadouken : public SpecialMove {
public:
    std::string moveName() const override { return "HADOUKEN"; }
    void execute(const std::string& f) const override {
        std::cout << f << " lanca " << moveName()
                  << "!  Dano: 35\n";
    }
};

class Shoryuken : public SpecialMove {
public:
    std::string moveName() const override { return "SHORYUKEN"; }
    void execute(const std::string& f) const override {
        std::cout << f << " executa " << moveName()
                  << "!  Dano: 50\n";
    }
};

class SpinningBirdKick : public SpecialMove {
public:
    std::string moveName() const override {
        return "SPINNING BIRD KICK"; }
    void execute(const std::string& f) const override {
        std::cout << f << " aplica " << moveName()
                  << "!  Dano: 42\n";
    }
};

class SonicBoom : public SpecialMove {
public:
    std::string moveName() const override { return "SONIC BOOM"; }
    void execute(const std::string& f) const override {
        std::cout << f << " dispara " << moveName()
                  << "!  Dano: 38\n";
    }
};

// ── Creator abstrato: Escola de Luta ─────────────────────
class FightingStyle {
protected:
    std::string fighterName;
public:
    explicit FightingStyle(const std::string& name)
        : fighterName(name) {}

    // Factory Method — subclasse decide o produto
    virtual std::unique_ptr<SpecialMove>
        createSpecialMove() const = 0;

    // Template Method — usa o factory method internamente
    void performCombo(int hits) const {
        auto move = createSpecialMove();
        std::cout << "--- " << fighterName
                  << " x" << hits << " ---\n";
        for (int i = 0; i < hits; ++i)
            move->execute(fighterName);
        std::cout << "\n";
    }

    virtual ~FightingStyle() = default;
};

// ── Creators concretos ────────────────────────────────────
class ShotokenStyle : public FightingStyle {
public:
    using FightingStyle::FightingStyle;
    std::unique_ptr<SpecialMove>
    createSpecialMove() const override {
        return std::make_unique<Hadouken>();
    }
};

class DragonStyle : public FightingStyle {
public:
    using FightingStyle::FightingStyle;
    std::unique_ptr<SpecialMove>
    createSpecialMove() const override {
        return std::make_unique<Shoryuken>();
    }
};

class KickStyle : public FightingStyle {
public:
    using FightingStyle::FightingStyle;
    std::unique_ptr<SpecialMove>
    createSpecialMove() const override {
        return std::make_unique<SpinningBirdKick>();
    }
};

class ChargeStyle : public FightingStyle {
public:
    using FightingStyle::FightingStyle;
    std::unique_ptr<SpecialMove>
    createSpecialMove() const override {
        return std::make_unique<SonicBoom>();
    }
};

// ── Main ──────────────────────────────────────────────────
int main() {
    std::vector<std::unique_ptr<FightingStyle>> fighters;
    fighters.push_back(
        std::make_unique<ShotokenStyle>("Ryu"));
    fighters.push_back(
        std::make_unique<DragonStyle>("Ken"));
    fighters.push_back(
        std::make_unique<KickStyle>("Chun-Li"));
    fighters.push_back(
        std::make_unique<ChargeStyle>("Guile"));

    for (const auto& f : fighters)
        f->performCombo(2);

    return 0;
}