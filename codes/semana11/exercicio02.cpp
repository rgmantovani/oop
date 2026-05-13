// ✅ Exercício 2 — Configuração Singleton

#include <iostream>
#include <string>
#include <map>

// ── Singleton ────────────────────────────────────────────
class Configuracao {
    std::map<std::string, std::string> dados_ = {
        {"dificuldade", "normal"},
        {"volume",      "80"},
        {"idioma",      "pt-BR"}
    };
    Configuracao() = default;

public:
    Configuracao(const Configuracao&)            = delete;
    Configuracao& operator=(const Configuracao&) = delete;

    static Configuracao& instancia() {
        static Configuracao inst;
        return inst;
    }

    void alterar(const std::string& chave,
                 const std::string& valor) {
        dados_[chave] = valor;
    }

    std::string obter(const std::string& chave) const {
        return dados_.at(chave);
    }

    void exibir() const {
        for (const auto& [k, v] : dados_)
            std::cout << "  [Config] "
                      << k << " = " << v << "\n";
    }
};

// ── Classes consumidoras ─────────────────────────────────
class MenuPrincipal {
public:
    void aplicar_configuracoes() {
        auto& cfg = Configuracao::instancia();
        cfg.alterar("dificuldade", "dificil");
        cfg.alterar("volume",      "60");
        std::cout << "[Menu] Configurações alteradas"
                     " pelo jogador\n";
        cfg.exibir();
    }
};

class Masmorra {
public:
    void iniciar() {
        std::cout << "\n[Masmorra] Lendo configurações"
                     " do jogo...\n";
        Configuracao::instancia().exibir();
    }
};

// ── Main ─────────────────────────────────────────────────
int main() {
    MenuPrincipal menu;
    Masmorra      masmorra;

    menu.aplicar_configuracoes();
    masmorra.iniciar();   // ✅ enxerga "dificil" e volume 60

    auto& a = Configuracao::instancia();
    auto& b = Configuracao::instancia();
    std::cout << "\nMesma instância? "
              << (&a == &b ? "True ✓" : "False ✗") << "\n";
    return 0;
}