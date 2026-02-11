/*
Semana 2: Encapsulamento e Validação de Dados
Exemplo: Classe Jogador com encapsulamento em C++

Conceitos abordados:
- Atributos privados
- Getters e Setters
- Validação de dados
- Sobrecarga do operador <<
- Tratamento de exceções
*/

#include <iostream>
#include <string>
#include <stdexcept>
#include <iomanip>

using namespace std;

// ============================================
// Classe Jogador com Encapsulamento
// ============================================

class Jogador {
private:
    string _nome;
    int _nivel;
    int _hp;
    int _hp_maximo;
    
    // Método privado auxiliar
    string criar_barra_hp() const {
        int percentual = (_hp * 100) / _hp_maximo;
        int barras_cheias = percentual / 10;
        int barras_vazias = 10 - barras_cheias;
        
        string barra = "[";
        for (int i = 0; i < barras_cheias; i++) barra += "█";
        for (int i = 0; i < barras_vazias; i++) barra += "░";
        barra += "] " + to_string(_hp) + "/" + to_string(_hp_maximo);
        
        return barra;
    }

public:
    // Construtor
    Jogador(string nome, int nivel = 1, int hp = 100) {
        set_nome(nome);
        set_nivel(nivel);
        _hp_maximo = hp;
        _hp = hp;
    }
    
    // ========================================
    // Getters
    // ========================================
    
    string get_nome() const {
        return _nome;
    }
    
    int get_nivel() const {
        return _nivel;
    }
    
    int get_hp() const {
        return _hp;
    }
    
    int get_hp_maximo() const {
        return _hp_maximo;
    }
    
    // ========================================
    // Setters com Validação
    // ========================================
    
    void set_nome(string nome) {
        if (nome.empty() || nome.find_first_not_of(' ') == string::npos) {
            throw invalid_argument("Nome não pode ser vazio");
        }
        _nome = nome;
    }
    
    void set_nivel(int nivel) {
        if (nivel < 1) {
            throw invalid_argument("Nível não pode ser menor que 1");
        }
        if (nivel > 100) {
            throw invalid_argument("Nível máximo é 100");
        }
        _nivel = nivel;
    }
    
    void set_hp(int hp) {
        if (hp < 0) {
            _hp = 0;
        } else if (hp > _hp_maximo) {
            _hp = _hp_maximo;
        } else {
            _hp = hp;
        }
    }
    
    void set_hp_maximo(int hp_maximo) {
        if (hp_maximo < 1) {
            throw invalid_argument("HP máximo deve ser positivo");
        }
        _hp_maximo = hp_maximo;
        if (_hp > _hp_maximo) {
            _hp = _hp_maximo;
        }
    }
    
    // ========================================
    // Métodos Públicos
    // ========================================
    
    void receber_dano(int dano) {
        if (dano < 0) {
            throw invalid_argument("Dano não pode ser negativo");
        }
        
        set_hp(_hp - dano);
        cout << _nome << " recebeu " << dano << " de dano! HP: " 
             << _hp << "/" << _hp_maximo << endl;
        
        if (_hp == 0) {
            cout << "💀 " << _nome << " foi derrotado!" << endl;
        }
    }
    
    void curar(int quantidade) {
        if (quantidade < 0) {
            throw invalid_argument("Cura não pode ser negativa");
        }
        
        int hp_anterior = _hp;
        set_hp(_hp + quantidade);
        int hp_recuperado = _hp - hp_anterior;
        
        cout << "❤️  " << _nome << " recuperou " << hp_recuperado 
             << " HP! HP: " << _hp << "/" << _hp_maximo << endl;
    }
    
    bool esta_vivo() const {
        return _hp > 0;
    }
    
    void exibir_status() const {
        cout << *this;
    }
    
    // ========================================
    // Sobrecarga do operador <<
    // ========================================
    
    friend ostream& operator<<(ostream& os, const Jogador& j) {
        string status = j.esta_vivo() ? "VIVO" : "MORTO";
        string barra_hp = j.criar_barra_hp();
        
        os << "\n╔════════════════════════════════════════╗\n";
        os << "║       STATUS DO JOGADOR                ║\n";
        os << "╠════════════════════════════════════════╣\n";
        os << "║ Nome:   " << setw(30) << left << j._nome << " ║\n";
        os << "║ Nível:  " << setw(30) << left << j._nivel << " ║\n";
        os << "║ Status: " << setw(30) << left << status << " ║\n";
        os << "║ HP:     " << barra_hp << "\n";
        os << "╚════════════════════════════════════════╝\n";
        
        return os;
    }
};

// ============================================
// Programa de Teste
// ============================================

int main() {
    cout << "============================================================" << endl;
    cout << "SEMANA 2: Encapsulamento e Validação de Dados" << endl;
    cout << "============================================================" << endl;
    cout << endl;
    
    try {
        // Criando jogador
        Jogador jogador("Thorin", 10, 200);
        jogador.exibir_status();
        
        // Testando validações
        cout << "\n>>> Testando validações:\n" << endl;
        
        try {
            jogador.set_nivel(-5);
        } catch (const invalid_argument& e) {
            cout << "❌ Erro capturado: " << e.what() << endl;
        }
        
        try {
            jogador.set_nome("");
        } catch (const invalid_argument& e) {
            cout << "❌ Erro capturado: " << e.what() << endl;
        }
        
        try {
            jogador.receber_dano(-10);
        } catch (const invalid_argument& e) {
            cout << "❌ Erro capturado: " << e.what() << endl;
        }
        
        // Testando HP com validação automática
        cout << "\n>>> Testando controle de HP:\n" << endl;
        jogador.receber_dano(50);
        jogador.curar(30);
        jogador.curar(200);  // Tenta curar além do máximo
        
        jogador.exibir_status();
        
        // Testando dano fatal
        cout << "\n>>> Testando dano fatal:\n" << endl;
        jogador.receber_dano(300);
        jogador.exibir_status();
        
        // Tentando curar jogador morto
        cout << "\n>>> Tentando curar jogador morto:\n" << endl;
        jogador.curar(50);
        jogador.exibir_status();
        
    } catch (const exception& e) {
        cerr << "Erro fatal: " << e.what() << endl;
        return 1;
    }
    
    return 0;
}

/*
Para compilar e executar:
g++ -std=c++17 -o jogador_encapsulado jogador_encapsulado.cpp
./jogador_encapsulado
*/
