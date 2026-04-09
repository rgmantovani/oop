# Gabarito — POO: Construtores e Destrutores
### C++ e Python · Nível Médio e Avançado

---

## Exercício 1 — Banco de dados de livros

**Conceitos:** construtor com parâmetros, destrutor básico, `__init__` e `__del__`

---

### C++

```cpp
#include <iostream>
#include <string>
#include <vector>

class Livro {
public:
    std::string titulo;
    std::string autor;
    int ano;

    // Construtor com todos os parâmetros
    Livro(const std::string& titulo, const std::string& autor, int ano)
        : titulo(titulo), autor(autor), ano(ano) {
        std::cout << "[+] Livro criado: " << titulo << "\n";
    }

    // Construtor sem ano (sobrecarga)
    Livro(const std::string& titulo, const std::string& autor)
        : titulo(titulo), autor(autor), ano(0) {
        std::cout << "[+] Livro criado (sem ano): " << titulo << "\n";
    }

    // Destrutor
    ~Livro() {
        std::cout << "[-] Livro destruído: " << titulo << "\n";
    }

    void exibir() const {
        std::cout << "\"" << titulo << "\" - " << autor;
        if (ano > 0) std::cout << " (" << ano << ")";
        std::cout << "\n";
    }
};

int main() {
    std::cout << "=== Criando livros em vetor ===\n";
    std::vector<Livro> biblioteca;
    biblioteca.emplace_back("Dom Casmurro", "Machado de Assis", 1899);
    biblioteca.emplace_back("O Cortiço", "Aluísio Azevedo");
    biblioteca.emplace_back("Capitães da Areia", "Jorge Amado", 1937);

    std::cout << "\n=== Catálogo ===\n";
    for (const auto& livro : biblioteca)
        livro.exibir();

    std::cout << "\n=== Fim do main — destruição do vetor ===\n";
    // Os destrutores são chamados aqui, na ordem inversa da criação
    return 0;
}
```

**Saída esperada (destruição na ordem inversa):**
```
[+] Livro criado: Dom Casmurro
[+] Livro criado (sem ano): O Cortiço
[+] Livro criado: Capitães da Areia
...
[-] Livro destruído: Capitães da Areia
[-] Livro destruído: O Cortiço
[-] Livro destruído: Dom Casmurro
```

---

### Python

```python
class Livro:
    def __init__(self, titulo: str, autor: str, ano: int = 0):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        print(f"[+] Livro criado: {self.titulo}")

    def __del__(self):
        print(f"[-] Livro destruído: {self.titulo}")

    def exibir(self):
        info = f'"{self.titulo}" - {self.autor}'
        if self.ano:
            info += f" ({self.ano})"
        print(info)


# Uso
biblioteca = [
    Livro("Dom Casmurro", "Machado de Assis", 1899),
    Livro("O Cortiço", "Aluísio Azevedo"),        # ano omitido → padrão 0
    Livro("Capitães da Areia", "Jorge Amado", 1937),
]

print("\n=== Catálogo ===")
for livro in biblioteca:
    livro.exibir()

print("\n=== Limpando lista ===")
biblioteca.clear()   # remove referências → GC pode chamar __del__
```

> **Nota:** Em Python, `__del__` não tem chamada garantida. Para fins didáticos, `lista.clear()` ou `del objeto` geralmente dispara o coletor, mas o comportamento exato depende do interpretador.

---

---

## Exercício 2 — Contador de instâncias

**Conceitos:** atributo estático, construtor/destrutor como eventos de ciclo de vida

---

### C++

```cpp
#include <iostream>
#include <string>

class Sensor {
private:
    static int total;   // atributo de classe compartilhado
    std::string nome;

public:
    Sensor(const std::string& nome) : nome(nome) {
        ++total;
        std::cout << "[+] Sensor \"" << nome << "\" ligado. Total ativo: " << total << "\n";
    }

    ~Sensor() {
        --total;
        std::cout << "[-] Sensor \"" << nome << "\" desligado. Total ativo: " << total << "\n";
    }

    static int getTotalAtivo() { return total; }
};

// Definição do atributo estático fora da classe (obrigatório em C++)
int Sensor::total = 0;

int main() {
    std::cout << "=== Escopo externo ===\n";
    Sensor s1("Temperatura");
    Sensor s2("Pressão");

    {
        std::cout << "\n=== Escopo interno ===\n";
        Sensor s3("Umidade");
        Sensor s4("Vibração");
        std::cout << "Sensores ativos agora: " << Sensor::getTotalAtivo() << "\n";
    }   // s3 e s4 são destruídos aqui

    std::cout << "\n=== Voltando ao escopo externo ===\n";
    std::cout << "Sensores ativos agora: " << Sensor::getTotalAtivo() << "\n";

    return 0;
}   // s1 e s2 são destruídos aqui
```

---

### Python

```python
class Sensor:
    _total = 0  # variável de classe (equivalente ao static)

    def __init__(self, nome: str):
        self.nome = nome
        Sensor._total += 1
        print(f"[+] Sensor '{self.nome}' ligado. Total ativo: {Sensor._total}")

    def __del__(self):
        Sensor._total -= 1
        print(f"[-] Sensor '{self.nome}' desligado. Total ativo: {Sensor._total}")

    @classmethod
    def get_total_ativo(cls) -> int:
        return cls._total


# Simulando escopos com blocos explícitos
s1 = Sensor("Temperatura")
s2 = Sensor("Pressão")

print("\n--- Criando sensores temporários ---")
s3 = Sensor("Umidade")
s4 = Sensor("Vibração")
print(f"Sensores ativos: {Sensor.get_total_ativo()}")

print("\n--- Deletando sensores temporários ---")
del s3
del s4
print(f"Sensores ativos: {Sensor.get_total_ativo()}")

print("\n--- Fim do programa ---")
del s1
del s2
```

---

---

## Exercício 3 — Gerenciador de arquivo (RAII)

**Conceitos:** RAII, destrutor garantindo liberação de recurso, segurança com exceções

*(Este exercício é exclusivo de C++; o exercício 4 cobre o equivalente Python)*

---

### C++

```cpp
#include <iostream>
#include <stdexcept>
#include <cstdio>

class GerenciadorArquivo {
private:
    FILE* arquivo;
    std::string caminho;

public:
    GerenciadorArquivo(const std::string& caminho, const std::string& modo)
        : caminho(caminho) {
        arquivo = fopen(caminho.c_str(), modo.c_str());
        if (!arquivo)
            throw std::runtime_error("Não foi possível abrir: " + caminho);
        std::cout << "[+] Arquivo aberto: " << caminho << "\n";
    }

    ~GerenciadorArquivo() {
        if (arquivo) {
            fclose(arquivo);
            std::cout << "[-] Arquivo fechado: " << caminho << "\n";
        }
    }

    void escrever(const std::string& texto) {
        fputs(texto.c_str(), arquivo);
    }

    // Desabilitar cópia para evitar double-free
    GerenciadorArquivo(const GerenciadorArquivo&) = delete;
    GerenciadorArquivo& operator=(const GerenciadorArquivo&) = delete;
};

void processarComExcecao() {
    GerenciadorArquivo ga("teste.txt", "w");
    ga.escrever("Linha 1\n");
    ga.escrever("Linha 2\n");
    throw std::runtime_error("Erro simulado durante processamento!");
    // O destrutor de 'ga' é chamado aqui mesmo com a exceção
}

int main() {
    std::cout << "=== Uso normal ===\n";
    {
        GerenciadorArquivo ga("normal.txt", "w");
        ga.escrever("Conteúdo normal\n");
    }   // arquivo fechado aqui

    std::cout << "\n=== Uso com exceção ===\n";
    try {
        processarComExcecao();
    } catch (const std::exception& e) {
        std::cout << "Exceção capturada: " << e.what() << "\n";
        std::cout << "(Arquivo foi fechado mesmo assim pelo destrutor!)\n";
    }

    return 0;
}
```

---

---

## Exercício 4 — Context manager manual (Python)

**Conceitos:** `__init__`, `__del__`, `__enter__`, `__exit__`, diferença entre os mecanismos

*(Exclusivo Python)*

---

### Python

```python
class ConexaoSimulada:
    def __init__(self, host: str):
        self.host = host
        self._conectado = False
        self._conectar()

    def _conectar(self):
        self._conectado = True
        print(f"[+] Conectado a {self.host}")

    def _desconectar(self):
        if self._conectado:
            self._conectado = False
            print(f"[-] Desconectado de {self.host}")

    def enviar(self, mensagem: str):
        if not self._conectado:
            raise RuntimeError("Sem conexão!")
        print(f"  >> Enviando para {self.host}: {mensagem}")

    # --- Mecanismo 1: __del__ (não confiável) ---
    def __del__(self):
        print(f"[__del__] chamado para {self.host}")
        self._desconectar()

    # --- Mecanismo 2: context manager (confiável) ---
    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._desconectar()
        # retornar False propaga exceções; True as suprime
        return False


print("=== Usando __del__ (não determinístico) ===")
c1 = ConexaoSimulada("servidor1.local")
c1.enviar("Olá")
del c1   # pode chamar __del__ imediatamente... ou não

print("\n=== Usando 'with' (determinístico) ===")
with ConexaoSimulada("servidor2.local") as c2:
    c2.enviar("Mensagem importante")
    # desconexão garantida ao sair do bloco, mesmo com exceção
print("(Conexão já foi fechada aqui)")

print("\n=== 'with' com exceção interna ===")
try:
    with ConexaoSimulada("servidor3.local") as c3:
        c3.enviar("Antes do erro")
        raise ValueError("Falha simulada!")
        c3.enviar("Nunca enviado")
except ValueError as e:
    print(f"Exceção capturada: {e}")
    print("(Conexão foi fechada mesmo assim pelo __exit__)")
```

---

---

## Exercício 5 — Lista encadeada com RAII (C++)

**Conceitos:** destrutor recursivo, construtor de cópia (deep copy), vazamento de memória

*(Exclusivo C++)*

---

### C++

```cpp
#include <iostream>

// Nó da lista — libera o próximo em cascata
struct No {
    int valor;
    No* proximo;

    No(int v) : valor(v), proximo(nullptr) {}

    ~No() {
        // ATENÇÃO: destrutores recursivos podem causar stack overflow
        // em listas muito longas. Ver nota abaixo.
        delete proximo;   // dispara ~No() do próximo em cascata
    }
};

class ListaEncadeada {
private:
    No* cabeca;

    // Copia profunda auxiliar
    No* copiarCadeia(No* origem) {
        if (!origem) return nullptr;
        No* novo = new No(origem->valor);
        novo->proximo = copiarCadeia(origem->proximo);
        return novo;
    }

public:
    ListaEncadeada() : cabeca(nullptr) {}

    // Construtor de cópia — deep copy
    ListaEncadeada(const ListaEncadeada& outra)
        : cabeca(copiarCadeia(outra.cabeca)) {
        std::cout << "[cópia] Lista copiada.\n";
    }

    // Destrutor — basta deletar a cabeça; a cascata cuida do resto
    ~ListaEncadeada() {
        delete cabeca;
    }

    void inserirFrente(int valor) {
        No* novo = new No(valor);
        novo->proximo = cabeca;
        cabeca = novo;
    }

    void imprimir() const {
        No* atual = cabeca;
        while (atual) {
            std::cout << atual->valor;
            if (atual->proximo) std::cout << " -> ";
            atual = atual->proximo;
        }
        std::cout << "\n";
    }
};

int main() {
    ListaEncadeada lista1;
    lista1.inserirFrente(30);
    lista1.inserirFrente(20);
    lista1.inserirFrente(10);

    std::cout << "Lista 1: ";
    lista1.imprimir();

    // Cópia profunda
    ListaEncadeada lista2 = lista1;
    lista2.inserirFrente(5);

    std::cout << "Lista 1 após cópia: ";
    lista1.imprimir();   // Não deve ser afetada pela lista2
    std::cout << "Lista 2: ";
    lista2.imprimir();

    // Destrutores chamados automaticamente ao fim do escopo
    // lista2 → lista1 (cada um libera sua própria cadeia de nós)
    return 0;
}

/*
 * NOTA SOBRE STACK OVERFLOW:
 * Com listas de 100.000+ nós, o destrutor recursivo pode estourar a pilha.
 * Solução: destrutor iterativo na classe Lista:
 *
 * ~ListaEncadeada() {
 *     while (cabeca) {
 *         No* tmp = cabeca->proximo;
 *         cabeca->proximo = nullptr;  // evita recursão no ~No
 *         delete cabeca;
 *         cabeca = tmp;
 *     }
 * }
 */
```

---

---

## Exercício 6 — Pool de memória (C++)

**Conceitos:** placement new, destrutor explícito, gerenciamento manual de memória

*(Exclusivo C++)*

---

### C++

```cpp
#include <iostream>
#include <new>       // para placement new
#include <cassert>

class Tarefa {
public:
    int id;
    std::string descricao;

    Tarefa(int id, const std::string& desc) : id(id), descricao(desc) {
        std::cout << "  [Tarefa] Construída: #" << id << "\n";
    }

    ~Tarefa() {
        std::cout << "  [Tarefa] Destruída: #" << id << "\n";
    }

    void executar() {
        std::cout << "  Executando tarefa #" << id << ": " << descricao << "\n";
    }
};

class PoolMemoria {
private:
    static const int CAPACIDADE = 4;
    char* bloco;                    // buffer bruto de bytes
    Tarefa* slots[CAPACIDADE];      // rastreia objetos construídos
    int quantidade;

public:
    PoolMemoria() : quantidade(0) {
        bloco = new char[CAPACIDADE * sizeof(Tarefa)];
        for (auto& s : slots) s = nullptr;
        std::cout << "[Pool] Bloco alocado (" << CAPACIDADE * sizeof(Tarefa) << " bytes)\n";
    }

    ~PoolMemoria() {
        // Chamar destrutores manualmente antes de liberar o bloco
        for (int i = 0; i < quantidade; ++i) {
            if (slots[i]) {
                slots[i]->~Tarefa();   // destrutor explícito
                slots[i] = nullptr;
            }
        }
        delete[] bloco;
        std::cout << "[Pool] Bloco liberado\n";
    }

    Tarefa* criar(int id, const std::string& desc) {
        assert(quantidade < CAPACIDADE && "Pool cheio!");
        // Placement new: constrói o objeto no endereço calculado dentro do bloco
        void* endereco = bloco + quantidade * sizeof(Tarefa);
        Tarefa* t = new (endereco) Tarefa(id, desc);
        slots[quantidade++] = t;
        return t;
    }

    // Sem cópia
    PoolMemoria(const PoolMemoria&) = delete;
    PoolMemoria& operator=(const PoolMemoria&) = delete;
};

int main() {
    PoolMemoria pool;

    Tarefa* t1 = pool.criar(1, "Processar pagamento");
    Tarefa* t2 = pool.criar(2, "Enviar e-mail");
    Tarefa* t3 = pool.criar(3, "Gerar relatório");

    t1->executar();
    t2->executar();
    t3->executar();

    std::cout << "\n[main] Fim do escopo — destruindo pool\n";
    // O destrutor do pool chama ~Tarefa() para cada slot, depois libera o bloco
    return 0;
}
```

---

---

## Exercício 7 — Registro de objetos ativos

**Conceitos:** construtor/destrutor interagindo com estado global, rastreamento de ciclo de vida

---

### C++

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

// Declaração antecipada
class Processo;

class Gerenciador {
private:
    std::vector<Processo*> ativos;

public:
    static Gerenciador& instancia() {
        static Gerenciador g;
        return g;
    }

    void registrar(Processo* p)   { ativos.push_back(p); }
    void remover(Processo* p) {
        ativos.erase(std::remove(ativos.begin(), ativos.end(), p), ativos.end());
    }

    void listarAtivos() const;  // implementado após Processo
};

class Processo {
public:
    std::string nome;
    int pid;

    Processo(const std::string& nome, int pid) : nome(nome), pid(pid) {
        Gerenciador::instancia().registrar(this);
        std::cout << "[+] Processo iniciado: " << nome << " (PID " << pid << ")\n";
    }

    ~Processo() {
        Gerenciador::instancia().remover(this);
        std::cout << "[-] Processo encerrado: " << nome << " (PID " << pid << ")\n";
    }
};

void Gerenciador::listarAtivos() const {
    std::cout << "--- Processos ativos (" << ativos.size() << ") ---\n";
    for (const auto* p : ativos)
        std::cout << "  " << p->nome << " (PID " << p->pid << ")\n";
}

int main() {
    Processo p1("init", 1);
    Processo p2("nginx", 1024);

    {
        Processo p3("worker-1", 2048);
        Processo p4("worker-2", 2049);
        Gerenciador::instancia().listarAtivos();
    }   // p3 e p4 destruídos aqui

    std::cout << "\n";
    Gerenciador::instancia().listarAtivos();

    return 0;
}
```

---

### Python

```python
class Gerenciador:
    _ativos: list = []

    @classmethod
    def registrar(cls, processo):
        cls._ativos.append(processo)

    @classmethod
    def remover(cls, processo):
        try:
            cls._ativos.remove(processo)
        except ValueError:
            pass  # já removido (pode acontecer com __del__ do GC)

    @classmethod
    def listar_ativos(cls):
        print(f"--- Processos ativos ({len(cls._ativos)}) ---")
        for p in cls._ativos:
            print(f"  {p.nome} (PID {p.pid})")


class Processo:
    def __init__(self, nome: str, pid: int):
        self.nome = nome
        self.pid = pid
        Gerenciador.registrar(self)
        print(f"[+] Processo iniciado: {nome} (PID {pid})")

    def __del__(self):
        Gerenciador.remover(self)
        print(f"[-] Processo encerrado: {self.nome} (PID {self.pid})")


p1 = Processo("init", 1)
p2 = Processo("nginx", 1024)
p3 = Processo("worker-1", 2048)
p4 = Processo("worker-2", 2049)

Gerenciador.listar_ativos()

print("\n--- Encerrando workers ---")
del p3
del p4

print()
Gerenciador.listar_ativos()

print("\n--- Fim do programa ---")
del p1
del p2
```

---

---

## Exercício 8 — Construtor de movimento (Regra dos 5) (C++)

**Conceitos:** Regra dos 5, move semantics, `std::move`, desempenho de cópia vs. movimento

*(Exclusivo C++)*

---

### C++

```cpp
#include <iostream>
#include <cstring>
#include <utility>   // std::move

class Buffer {
private:
    int* dados;
    size_t tamanho;

public:
    // 1. Construtor
    Buffer(size_t tam) : tamanho(tam), dados(new int[tam]) {
        std::fill(dados, dados + tamanho, 0);
        std::cout << "[Buffer] Construído, tam=" << tamanho << "\n";
    }

    // 2. Destrutor
    ~Buffer() {
        delete[] dados;
        std::cout << "[Buffer] Destruído, tam=" << tamanho << "\n";
    }

    // 3. Construtor de cópia (deep copy)
    Buffer(const Buffer& outro) : tamanho(outro.tamanho), dados(new int[outro.tamanho]) {
        std::copy(outro.dados, outro.dados + tamanho, dados);
        std::cout << "[Buffer] COPIADO, tam=" << tamanho << "\n";
    }

    // 4. Operador de atribuição por cópia
    Buffer& operator=(const Buffer& outro) {
        if (this == &outro) return *this;
        delete[] dados;
        tamanho = outro.tamanho;
        dados = new int[tamanho];
        std::copy(outro.dados, outro.dados + tamanho, dados);
        std::cout << "[Buffer] Atribuição por cópia, tam=" << tamanho << "\n";
        return *this;
    }

    // 5. Construtor de movimento (transfere ownership, não copia)
    Buffer(Buffer&& outro) noexcept
        : tamanho(outro.tamanho), dados(outro.dados) {
        outro.dados = nullptr;   // invalida o original
        outro.tamanho = 0;
        std::cout << "[Buffer] MOVIDO (sem cópia de dados)\n";
    }

    // 6. Operador de atribuição por movimento
    Buffer& operator=(Buffer&& outro) noexcept {
        if (this == &outro) return *this;
        delete[] dados;
        dados = outro.dados;
        tamanho = outro.tamanho;
        outro.dados = nullptr;
        outro.tamanho = 0;
        std::cout << "[Buffer] Atribuição por movimento\n";
        return *this;
    }

    void set(size_t i, int val) { if (i < tamanho) dados[i] = val; }
    int get(size_t i) const    { return (i < tamanho) ? dados[i] : -1; }
    size_t getTamanho() const  { return tamanho; }
};

Buffer criarBuffer() {
    Buffer temp(5);
    temp.set(0, 42);
    return temp;   // NRVO ou move acontece aqui
}

int main() {
    std::cout << "=== Cópia ===\n";
    Buffer b1(3);
    b1.set(0, 10); b1.set(1, 20); b1.set(2, 30);
    Buffer b2 = b1;   // construtor de cópia — aloca nova memória
    b2.set(0, 99);
    std::cout << "b1[0]=" << b1.get(0) << "  b2[0]=" << b2.get(0) << "\n";

    std::cout << "\n=== Movimento ===\n";
    Buffer b3(3);
    b3.set(0, 100);
    Buffer b4 = std::move(b3);   // construtor de movimento — sem cópia
    std::cout << "b3.tam=" << b3.getTamanho() << " (invalidado)\n";
    std::cout << "b4[0]=" << b4.get(0) << "\n";

    std::cout << "\n=== Retorno de função (NRVO/move) ===\n";
    Buffer b5 = criarBuffer();
    std::cout << "b5[0]=" << b5.get(0) << "\n";

    return 0;
}
```

---

---

## Exercício 9 — Finalização determinística com weakref (Python)

**Conceitos:** não-determinismo do `__del__`, referência circular, `weakref.finalize`

*(Exclusivo Python)*

---

### Python

```python
import gc
import weakref


class Recurso:
    """
    Demonstra três formas de finalização:
    1. __del__ puro — não determinístico, falha em referências circulares
    2. método close() explícito — determinístico, mas manual
    3. weakref.finalize — determinístico, não impede coleta pelo GC
    """

    def __init__(self, nome: str):
        self.nome = nome
        self._aberto = True
        print(f"[+] Recurso '{nome}' aberto")

        # Registra finalizador via weakref — não cria referência forte
        self._finalizador = weakref.finalize(
            self,
            Recurso._fechar_callback,
            nome   # passa o nome por valor (não referência ao objeto)
        )

    @staticmethod
    def _fechar_callback(nome: str):
        print(f"[weakref] Recurso '{nome}' finalizado de forma determinística")

    def __del__(self):
        print(f"[__del__] chamado para '{self.nome}' (pode não acontecer!)")

    def close(self):
        if self._aberto:
            self._aberto = False
            self._finalizador()  # dispara o finalizador manualmente
            print(f"[close] Recurso '{self.nome}' fechado explicitamente")


# ───────────────────────────────────────────────
print("=== Caso 1: Uso normal com del ===")
r1 = Recurso("banco-de-dados")
del r1   # normalmente chama __del__ imediatamente no CPython
gc.collect()

# ───────────────────────────────────────────────
print("\n=== Caso 2: Referência circular → __del__ pode falhar ===")
r2 = Recurso("arquivo-log")
r3 = Recurso("cache")
r2.parceiro = r3   # cria ciclo
r3.parceiro = r2   # r2 → r3 → r2 → ...

del r2
del r3
print("(após del r2, del r3 — __del__ talvez NÃO seja chamado ainda)")
print("Forçando coleta com gc.collect()...")
gc.collect()   # coleta o ciclo; weakref.finalize ainda funciona aqui

# ───────────────────────────────────────────────
print("\n=== Caso 3: Fechamento explícito com close() ===")
r4 = Recurso("conexão-redis")
r4.close()   # garantido, independente do GC
# weakref.finalize não chama de novo (já foi disparado)
del r4

# ───────────────────────────────────────────────
print("\n=== Resumo das garantias ===")
print("  __del__          : NÃO determinístico, falha em ciclos")
print("  close() explícito: Determinístico, mas requer disciplina do programador")
print("  weakref.finalize : Determinístico, seguro em ciclos, recomendado")
```

**Saída esperada (CPython):**
```
=== Caso 1: Uso normal com del ===
[+] Recurso 'banco-de-dados' aberto
[__del__] chamado para 'banco-de-dados' (pode não acontecer!)
[weakref] Recurso 'banco-de-dados' finalizado de forma determinística

=== Caso 2: Referência circular ...
[+] Recurso 'arquivo-log' aberto
[+] Recurso 'cache' aberto
(após del — __del__ talvez NÃO seja chamado ainda)
Forçando coleta...
[weakref] Recurso 'arquivo-log' finalizado de forma determinística
[weakref] Recurso 'cache' finalizado de forma determinística
...
```

---

---

## Resumo dos conceitos cobertos

| Exercício | C++ | Python |
|-----------|-----|--------|
| 1 – Livros | Construtor sobrecarregado, destrutor básico | `__init__` com default arg, `__del__` |
| 2 – Contador | `static` + construtor/destrutor | Variável de classe + `@classmethod` |
| 3 – Arquivo | RAII com `FILE*`, `= delete` | — |
| 4 – Conexão | — | `__enter__`/`__exit__`, `with` |
| 5 – Lista | Destrutor recursivo, deep copy, `= delete` | — |
| 6 – Pool | Placement `new`, destrutor explícito | — |
| 7 – Processos | Registro global, singleton estático | Variável de classe como registro |
| 8 – Buffer | Regra dos 5, `std::move`, `noexcept` | — |
| 9 – Recurso | — | `weakref.finalize`, `gc`, ciclos |
