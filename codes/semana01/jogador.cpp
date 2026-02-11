/*
Semana 1: Introdução à POO e Primeira Classe
Exemplo: Classe Jogador básica em C++

Conceitos abordados:
- Definição de classe
- Atributos de instância
- Métodos
- Construtores
- Separação interface (.h) e implementação (.cpp)
*/

#include <iostream>
#include <string>

using namespace std;

// ============================================
// Declaração da Classe Jogador
// ============================================

class Jogador {
private:
    string nome;
    int nivel;
    int hp;
    int hp_maximo;

public:
    // Construtores
    Jogador(string nome, int nivel = 1, int hp = 100);
    
    // Métodos
    void exibir_status() const;
    bool esta_vivo() const;
    void receber_dano(int dano);
    void curar(int quantidade);
    
    // Getters (para acesso aos atributos privados)
    string get_nome() const { return nome; }
    int get_nivel() const { return nivel; }
    int get_hp() const { return hp; }
    int get_hp_maximo() const { return hp_maximo; }
};

// ============================================
// Implementação dos Métodos
// ============================================

Jogador::Jogador(string nome, int nivel, int hp) {
    this->nome = nome;
    this->nivel = nivel;
    this->hp = hp;
    this->hp_maximo = hp;
}

void Jogador::exibir_status() const {
    cout << "=== Status do Jogador ===" << endl;
    cout << "Nome: " << nome << endl;
    cout << "Nível: " << nivel << endl;
    cout << "HP: " << hp << "/" << hp_maximo << endl;
    cout << "=========================" << endl;
}

bool Jogador::esta_vivo() const {
    return hp > 0;
}

void Jogador::receber_dano(int dano) {
    hp -= dano;
    if (hp < 0) {
        hp = 0;
    }
    cout << nome << " recebeu " << dano << " de dano!" << endl;
}

void Jogador::curar(int quantidade) {
    hp += quantidade;
    if (hp > hp_maximo) {
        hp = hp_maximo;
    }
    cout << nome << " recuperou " << quantidade << " HP!" << endl;
}

// ============================================
// Programa de Teste
// ============================================

int main() {
    cout << "==================================================" << endl;
    cout << "SEMANA 1: Classe Jogador Básica" << endl;
    cout << "==================================================" << endl;
    cout << endl;
    
    // Criando jogadores
    Jogador jogador1("Aragorn", 5, 150);
    Jogador jogador2("Legolas", 4, 120);
    Jogador jogador3("Gandalf");  // Usando valores padrão
    
    // Exibindo status inicial
    cout << ">>> Jogadores criados:" << endl << endl;
    jogador1.exibir_status();
    cout << endl;
    jogador2.exibir_status();
    cout << endl;
    jogador3.exibir_status();
    cout << endl;
    
    // Testando métodos
    cout << ">>> Testando combate:" << endl << endl;
    jogador1.receber_dano(30);
    jogador1.exibir_status();
    cout << endl;
    
    cout << jogador1.get_nome() << " está vivo? " 
         << (jogador1.esta_vivo() ? "Sim" : "Não") << endl;
    cout << endl;
    
    jogador1.curar(20);
    jogador1.exibir_status();
    cout << endl;
    
    // Simulando morte
    cout << ">>> Simulando dano fatal:" << endl << endl;
    jogador2.receber_dano(200);
    jogador2.exibir_status();
    cout << jogador2.get_nome() << " está vivo? " 
         << (jogador2.esta_vivo() ? "Sim" : "Não") << endl;
    cout << endl;
    
    return 0;
}

/*
Para compilar e executar:
g++ -std=c++17 -o jogador jogador.cpp
./jogador
*/
