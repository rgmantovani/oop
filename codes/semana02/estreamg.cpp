/*
 * EstreamG — Simulador de Loja de EGames
 * Implementação em C++17
 */

#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <numeric>
#include <sstream>
#include <iomanip>
#include <ctime>
#include <functional>

using namespace std;

// ─────────────────────────────────────────
//  Utilitários
// ─────────────────────────────────────────
static string dataHoraAtual() {
    time_t now = time(nullptr);
    char buf[32];
    strftime(buf, sizeof(buf), "%d/%m/%Y %H:%M:%S", localtime(&now));
    return string(buf);
}

static size_t hashSenha(const string& senha) {
    return hash<string>{}(senha);
}

static int contadorRecibo = 1;

// ─────────────────────────────────────────
//  JOGO
// ─────────────────────────────────────────
class Jogo {
public:
    Jogo(string titulo, string desenvolvedor, double preco, string categoria)
        : titulo_(move(titulo)), desenvolvedor_(move(desenvolvedor)),
          preco_(preco), categoria_(move(categoria)), ativo_(true) {}

    // ── getters ──────────────────────────
    const string& getTitulo()       const { return titulo_; }
    double        getPreco()        const { return preco_; }
    const string& getCategoria()    const { return categoria_; }
    const string& getDesenvolvedor()const { return desenvolvedor_; }
    bool          estaAtivo()       const { return ativo_; }

    // ── avaliações ───────────────────────
    bool avaliar(int nota) {
        if (!validarNota(nota)) {
            cout << "  [!] Nota invalida. Use inteiro entre 1 e 5.\n";
            return false;
        }
        avaliacoes_.push_back(nota);
        return true;
    }

    string mediaAvaliacoes() const {
        if (avaliacoes_.empty()) return "Sem avaliacoes";
        double media = accumulate(avaliacoes_.begin(), avaliacoes_.end(), 0.0)
                       / avaliacoes_.size();
        ostringstream oss;
        oss << fixed << setprecision(1) << media;
        return oss.str();
    }

    void desativar() { ativo_ = false; }

private:
    string titulo_, desenvolvedor_, categoria_;
    double preco_;
    vector<int> avaliacoes_;
    bool ativo_;

    bool validarNota(int nota) const {
        return nota >= 1 && nota <= 5;
    }
};

// ─────────────────────────────────────────
//  CUPOM
// ─────────────────────────────────────────
struct Data {
    int ano, mes, dia;
    bool operator<(const Data& o) const {
        if (ano != o.ano) return ano < o.ano;
        if (mes != o.mes) return mes < o.mes;
        return dia < o.dia;
    }
};

static Data dataHoje() {
    time_t now = time(nullptr);
    tm* t = localtime(&now);
    return { t->tm_year + 1900, t->tm_mon + 1, t->tm_mday };
}

class Cupom {
public:
    Cupom(string codigo, double percentual, Data validade,
          string categoriaRestrita = "", bool usoUnico = true)
        : codigo_(move(codigo)), percentual_(percentual),
          validade_(validade), categoriaRestrita_(move(categoriaRestrita)),
          usoUnico_(usoUnico), usado_(false) {}

    const string& getCodigo()            const { return codigo_; }
    double        getDesconto()          const { return percentual_; }
    const string& getCategoriaRestrita() const { return categoriaRestrita_; }

    bool estaValido() const {
        bool vencido = dataHoje().ano > validade_.ano ||
                       (dataHoje().ano == validade_.ano && dataHoje().mes > validade_.mes) ||
                       (dataHoje().ano == validade_.ano && dataHoje().mes == validade_.mes
                        && dataHoje().dia > validade_.dia);
        return !vencido && !(usoUnico_ && usado_);
    }

    bool aplicavelAoJogo(const Jogo& jogo) const {
        return categoriaRestrita_.empty() ||
               jogo.getCategoria() == categoriaRestrita_;
    }

    bool consumir() {
        if (!estaValido()) {
            cout << "  [!] Cupom '" << codigo_ << "' invalido ou ja utilizado.\n";
            return false;
        }
        usado_ = true;
        return true;
    }

private:
    string codigo_, categoriaRestrita_;
    double percentual_;
    Data   validade_;
    bool   usoUnico_, usado_;
};

// ─────────────────────────────────────────
//  ITEM CARRINHO
// ─────────────────────────────────────────
class ItemCarrinho {
public:
    explicit ItemCarrinho(Jogo* jogo)
        : jogo_(jogo), cupom_(nullptr) {}

    Jogo*  getJogo()  const { return jogo_; }
    Cupom* getCupom() const { return cupom_; }

    bool aplicarCupom(Cupom* cupom) {
        if (!cupom->estaValido()) {
            cout << "  [!] Cupom '" << cupom->getCodigo() << "' expirado ou ja usado.\n";
            return false;
        }
        if (!cupom->aplicavelAoJogo(*jogo_)) {
            cout << "  [!] Cupom '" << cupom->getCodigo()
                 << "' nao valido para categoria '"
                 << jogo_->getCategoria() << "'.\n";
            return false;
        }
        cupom_ = cupom;
        cout << "  [v] Cupom '" << cupom->getCodigo()
             << "' aplicado em '" << jogo_->getTitulo() << "'.\n";
        return true;
    }

    double getPrecoFinal() const {
        if (cupom_) {
            double desconto = jogo_->getPreco() * (cupom_->getDesconto() / 100.0);
            return jogo_->getPreco() - desconto;
        }
        return jogo_->getPreco();
    }

    double getDescontoAplicado() const {
        return jogo_->getPreco() - getPrecoFinal();
    }

private:
    Jogo*  jogo_;
    Cupom* cupom_;
};

// ─────────────────────────────────────────
//  CARRINHO
// ─────────────────────────────────────────
class Carrinho {
public:
    explicit Carrinho(const string& idUsuario) : idUsuario_(idUsuario) {}

    bool adicionar(Jogo* jogo) {
        if (buscarItem(jogo->getTitulo())) {
            cout << "  [!] '" << jogo->getTitulo() << "' ja esta no carrinho.\n";
            return false;
        }
        itens_.emplace_back(jogo);
        cout << "  [+] '" << jogo->getTitulo() << "' adicionado ao carrinho.\n";
        return true;
    }

    bool remover(const string& titulo) {
        auto it = find_if(itens_.begin(), itens_.end(),
            [&](const ItemCarrinho& i){ return i.getJogo()->getTitulo() == titulo; });
        if (it == itens_.end()) {
            cout << "  [!] '" << titulo << "' nao encontrado no carrinho.\n";
            return false;
        }
        itens_.erase(it);
        cout << "  [-] '" << titulo << "' removido do carrinho.\n";
        return true;
    }

    bool aplicarCupomItem(const string& titulo, Cupom* cupom) {
        ItemCarrinho* item = buscarItem(titulo);
        if (!item) {
            cout << "  [!] '" << titulo << "' nao esta no carrinho.\n";
            return false;
        }
        return item->aplicarCupom(cupom);
    }

    double getTotal() const {
        double total = 0;
        for (const auto& i : itens_) total += i.getPrecoFinal();
        return total;
    }

    double getEconomiaTotal() const {
        double eco = 0;
        for (const auto& i : itens_) eco += i.getDescontoAplicado();
        return eco;
    }

    void listar() const {
        if (itens_.empty()) { cout << "  Carrinho vazio.\n"; return; }
        cout << "\n  +----------------------------------------------+\n";
        cout <<   "  |            CARRINHO                          |\n";
        cout <<   "  +----------------------------------------------+\n";
        for (const auto& item : itens_) {
            Jogo* j = item.getJogo();
            string preco_str = (j->getPreco() == 0.0) ? "GRATIS" :
                               "R$ " + [&](){
                                   ostringstream o; o << fixed << setprecision(2) << j->getPreco();
                                   return o.str(); }();
            cout << "  | " << left << setw(30) << j->getTitulo()
                 << right << setw(12) << preco_str << "  |\n";
            if (item.getDescontoAplicado() > 0) {
                Cupom* c = item.getCupom();
                ostringstream desc;
                desc << fixed << setprecision(2) << item.getDescontoAplicado();
                cout << "  |   Cupom " << c->getCodigo()
                     << " (-" << (int)c->getDesconto() << "%)"
                     << "         -R$ " << desc.str() << "  |\n";
            }
        }
        cout << "  +----------------------------------------------+\n";
        double eco = getEconomiaTotal();
        if (eco > 0) {
            ostringstream o; o << fixed << setprecision(2) << eco;
            cout << "  | Economia total:            -R$ " << right << setw(9) << o.str() << "  |\n";
        }
        ostringstream tot; tot << fixed << setprecision(2) << getTotal();
        cout << "  | TOTAL:                      R$ " << right << setw(9) << tot.str() << "  |\n";
        cout << "  +----------------------------------------------+\n\n";
    }

    bool estaVazio()                        const { return itens_.empty(); }
    const vector<ItemCarrinho>& getItens()  const { return itens_; }
    void limpar()                                 { itens_.clear(); }

private:
    string idUsuario_;
    vector<ItemCarrinho> itens_;

    ItemCarrinho* buscarItem(const string& titulo) {
        for (auto& i : itens_)
            if (i.getJogo()->getTitulo() == titulo) return &i;
        return nullptr;
    }
};

// ─────────────────────────────────────────
//  BIBLIOTECA
// ─────────────────────────────────────────
class Biblioteca {
public:
    bool adicionarJogo(const string& titulo) {
        if (jogoNaBiblioteca(titulo)) return false;
        jogos_.push_back(titulo);
        horasJogadas_[titulo] = 0.0;
        return true;
    }

    bool possui(const string& titulo) const {
        return jogoNaBiblioteca(titulo);
    }

    bool registrarHoras(const string& titulo, double horas) {
        if (!jogoNaBiblioteca(titulo)) {
            cout << "  [!] '" << titulo << "' nao esta na sua biblioteca.\n";
            return false;
        }
        if (horas <= 0) { cout << "  [!] Horas devem ser positivas.\n"; return false; }
        horasJogadas_[titulo] += horas;
        return true;
    }

    double getHoras(const string& titulo) const {
        auto it = horasJogadas_.find(titulo);
        return (it != horasJogadas_.end()) ? it->second : 0.0;
    }

    void listar() const {
        if (jogos_.empty()) { cout << "  Biblioteca vazia.\n"; return; }
        vector<string> ordenados = jogos_;
        sort(ordenados.begin(), ordenados.end(),
             [&](const string& a, const string& b){
                 return getHoras(a) > getHoras(b); });
        cout << "\n  +----------------------------------------------+\n";
        cout <<   "  |           MINHA BIBLIOTECA                   |\n";
        cout <<   "  +----------------------------------------------+\n";
        for (const auto& t : ordenados) {
            ostringstream h; h << fixed << setprecision(1) << getHoras(t);
            cout << "  | " << left << setw(36) << t
                 << right << setw(6) << h.str() << "h  |\n";
        }
        cout << "  +----------------------------------------------+\n\n";
    }

private:
    vector<string> jogos_;
    map<string, double> horasJogadas_;

    bool jogoNaBiblioteca(const string& titulo) const {
        return find(jogos_.begin(), jogos_.end(), titulo) != jogos_.end();
    }
};

// ─────────────────────────────────────────
//  RECIBO
// ─────────────────────────────────────────
class Recibo {
public:
    Recibo(const string& nomeUsuario, const vector<ItemCarrinho>& itens)
        : idRecibo_("REC-" + to_string(contadorRecibo++)),
          nomeUsuario_(nomeUsuario),
          itensCopia_(itens),
          dataHora_(dataHoraAtual()) {
        totalPago_ = 0;
        totalEconomizado_ = 0;
        for (const auto& i : itensCopia_) {
            totalPago_      += i.getPrecoFinal();
            totalEconomizado_ += i.getDescontoAplicado();
        }
    }

    void exibir() const {
        cout << "\n  +----------------------------------------------+\n";
        cout << "  | RECIBO " << left << setw(38) << idRecibo_ << "|\n";
        cout << "  | Data: " << left << setw(40) << dataHora_ << "|\n";
        cout << "  | Cliente: " << left << setw(37) << nomeUsuario_ << "|\n";
        cout << "  +----------------------------------------------+\n";
        for (const auto& item : itensCopia_) {
            Jogo* j = item.getJogo();
            ostringstream pf; pf << fixed << setprecision(2) << item.getPrecoFinal();
            cout << "  | " << left << setw(30) << j->getTitulo()
                 << "R$ " << right << setw(9) << pf.str() << "  |\n";
            if (item.getDescontoAplicado() > 0) {
                ostringstream d; d << fixed << setprecision(2) << item.getDescontoAplicado();
                cout << "  |   desconto:               -R$ " << right << setw(8) << d.str() << "  |\n";
            }
        }
        cout << "  +----------------------------------------------+\n";
        if (totalEconomizado_ > 0) {
            ostringstream e; e << fixed << setprecision(2) << totalEconomizado_;
            cout << "  | Voce economizou:        R$ " << right << setw(12) << e.str() << "  |\n";
        }
        ostringstream t; t << fixed << setprecision(2) << totalPago_;
        cout << "  | TOTAL PAGO:             R$ " << right << setw(12) << t.str() << "  |\n";
        cout << "  +----------------------------------------------+\n\n";
    }

    double      getTotalPago() const { return totalPago_; }
    const string& getId()      const { return idRecibo_; }

private:
    string idRecibo_, nomeUsuario_, dataHora_;
    vector<ItemCarrinho> itensCopia_;
    double totalPago_, totalEconomizado_;
};

// ─────────────────────────────────────────
//  USUÁRIO
// ─────────────────────────────────────────
class Usuario {
public:
    Usuario(string nome, string email, const string& senha)
        : nome_(move(nome)), email_(move(email)),
          senhaHash_(hashSenha(senha)), saldo_(0.0),
          carrinho_(email_) {}

    // ── getters ──────────────────────────
    const string& getNome()  const { return nome_; }
    const string& getEmail() const { return email_; }
    double        getSaldo() const { return saldo_; }

    // ── saldo ────────────────────────────
    bool depositarSaldo(double valor) {
        if (valor <= 0) { cout << "  [!] Valor deve ser positivo.\n"; return false; }
        saldo_ += valor;
        cout << fixed << setprecision(2)
             << "  [v] R$ " << valor << " depositado. Saldo: R$ " << saldo_ << "\n";
        return true;
    }

    // ── carrinho ─────────────────────────
    bool adicionarAoCarrinho(Jogo* jogo) {
        if (biblioteca_.possui(jogo->getTitulo())) {
            cout << "  [!] Voce ja possui '" << jogo->getTitulo() << "' na biblioteca.\n";
            return false;
        }
        return carrinho_.adicionar(jogo);
    }

    bool removerDoCarrinho(const string& titulo) {
        return carrinho_.remover(titulo);
    }

    bool aplicarCupom(const string& titulo, Cupom* cupom) {
        return carrinho_.aplicarCupomItem(titulo, cupom);
    }

    void verCarrinho()   { carrinho_.listar(); }
    void verBiblioteca() { biblioteca_.listar(); }

    bool registrarHoras(const string& titulo, double horas) {
        return biblioteca_.registrarHoras(titulo, horas);
    }

    bool autenticar(const string& senha) const {
        return hashSenha(senha) == senhaHash_;
    }

    void adicionarRecibo(const Recibo& r) { historico_.push_back(r); }

    void verHistorico() const {
        if (historico_.empty()) { cout << "  Nenhuma compra ainda.\n"; return; }
        for (const auto& r : historico_) r.exibir();
    }

    // ── acesso interno para Loja ─────────
    Carrinho&   _getCarrinho()   { return carrinho_; }
    Biblioteca& _getBiblioteca() { return biblioteca_; }

    void _debitarSaldo(double valor) { saldo_ -= valor; }

private:
    string   nome_, email_;
    size_t   senhaHash_;
    double   saldo_;
    Carrinho  carrinho_;
    Biblioteca biblioteca_;
    vector<Recibo> historico_;
};

// ─────────────────────────────────────────
//  LOJA
// ─────────────────────────────────────────
class Loja {
public:
    explicit Loja(string nome = "EstreamG") : nome_(move(nome)) {}

    // ── cadastros ────────────────────────
    bool cadastrarJogo(Jogo* jogo) {
        if (buscarJogo(jogo->getTitulo())) {
            cout << "  [!] '" << jogo->getTitulo() << "' ja cadastrado.\n";
            return false;
        }
        catalogo_.push_back(jogo);
        cout << "  [v] '" << jogo->getTitulo() << "' adicionado ao catalogo.\n";
        return true;
    }

    Usuario* cadastrarUsuario(const string& nome, const string& email,
                               const string& senha) {
        if (usuarios_.count(email)) {
            cout << "  [!] Email '" << email << "' ja cadastrado.\n";
            return nullptr;
        }
        usuarios_.emplace(email, Usuario(nome, email, senha));
        cout << "  [v] Usuario '" << nome << "' cadastrado com sucesso.\n";
        return &usuarios_.at(email);
    }

    // ── acesso ───────────────────────────
    Usuario* login(const string& email, const string& senha) {
        auto it = usuarios_.find(email);
        if (it == usuarios_.end() || !it->second.autenticar(senha)) {
            cout << "  [!] Email ou senha incorretos.\n";
            return nullptr;
        }
        cout << "  [v] Bem-vindo(a), " << it->second.getNome() << "!\n";
        return &it->second;
    }

    Jogo* buscarJogo(const string& titulo) {
        for (auto* j : catalogo_)
            if (j->getTitulo() == titulo) return j;
        return nullptr;
    }

    // ── catálogo ─────────────────────────
    void listarCatalogo() const {
        cout << "\n  +------------------------------------------------------+\n";
        cout <<   "  |          " << nome_ << " -- CATALOGO                        |\n";
        cout <<   "  +------------------------------------------------------+\n";
        for (const auto* j : catalogo_) {
            if (!j->estaAtivo()) continue;
            string preco = (j->getPreco() == 0.0) ? "GRATIS" :
                           [&](){
                               ostringstream o;
                               o << "R$ " << fixed << setprecision(2) << j->getPreco();
                               return o.str(); }();
            cout << "  | " << left << setw(24) << j->getTitulo()
                 << setw(14) << j->getCategoria()
                 << right << setw(10) << preco
                 << "  * " << j->mediaAvaliacoes() << "  |\n";
        }
        cout << "  +------------------------------------------------------+\n\n";
    }

    vector<Jogo*> buscarPorCategoria(const string& cat) {
        vector<Jogo*> res;
        for (auto* j : catalogo_)
            if (j->getCategoria() == cat && j->estaAtivo()) res.push_back(j);
        cout << "\n  Jogos em '" << cat << "': " << res.size() << " encontrado(s).\n";
        for (auto* j : res)
            cout << "    * " << j->getTitulo() << " | R$ "
                 << fixed << setprecision(2) << j->getPreco()
                 << " | " << j->mediaAvaliacoes() << "\n";
        return res;
    }

    // ── compra ───────────────────────────
    Recibo* finalizarCompra(Usuario* usuario) {
        Carrinho&   carrinho   = usuario->_getCarrinho();
        Biblioteca& biblioteca = usuario->_getBiblioteca();

        if (carrinho.estaVazio()) {
            cout << "  [!] Carrinho esta vazio.\n"; return nullptr;
        }

        double total = carrinho.getTotal();
        if (usuario->getSaldo() < total) {
            cout << fixed << setprecision(2)
                 << "  [!] Saldo insuficiente. Saldo: R$ " << usuario->getSaldo()
                 << " | Total: R$ " << total << "\n";
            return nullptr;
        }

        for (const auto& item : carrinho.getItens()) {
            if (biblioteca.possui(item.getJogo()->getTitulo())) {
                cout << "  [!] '" << item.getJogo()->getTitulo()
                     << "' ja esta na sua biblioteca.\n";
                return nullptr;
            }
        }

        // Consume cupons
        for (const auto& item : carrinho.getItens())
            if (item.getCupom()) const_cast<Cupom*>(item.getCupom())->consumir();

        usuario->_debitarSaldo(total);

        for (const auto& item : carrinho.getItens())
            biblioteca.adicionarJogo(item.getJogo()->getTitulo());

        registrarVenda(carrinho.getItens());

        recibos_.emplace_back(usuario->getNome(), carrinho.getItens());
        usuario->adicionarRecibo(recibos_.back());

        carrinho.limpar();

        cout << fixed << setprecision(2)
             << "  [v] Compra finalizada! Saldo restante: R$ "
             << usuario->getSaldo() << "\n";
        return &recibos_.back();
    }

    // ── avaliação ────────────────────────
    bool avaliarJogo(const string& titulo, int nota, Usuario* usuario) {
        if (!usuario->_getBiblioteca().possui(titulo)) {
            cout << "  [!] Voce precisa possuir '" << titulo << "' para avalia-lo.\n";
            return false;
        }
        Jogo* jogo = buscarJogo(titulo);
        if (!jogo) return false;
        bool ok = jogo->avaliar(nota);
        if (ok) cout << "  [v] Avaliacao " << nota << "* registrada para '" << titulo << "'.\n";
        return ok;
    }

    // ── relatório ────────────────────────
    void relatorioVendas() const {
        double total = 0;
        for (const auto& r : recibos_) total += r.getTotalPago();
        cout << "\n  +----------------------------------------------+\n";
        cout <<   "  |         RELATORIO DE VENDAS                  |\n";
        cout <<   "  +----------------------------------------------+\n";
        cout << "  | Total de compras: " << left << setw(27) << recibos_.size() << "|\n";
        ostringstream tot; tot << fixed << setprecision(2) << total;
        cout << "  | Total arrecadado: R$ " << left << setw(24) << tot.str() << "|\n";
        cout << "  +----------------------------------------------+\n";
        cout << "  | Jogos mais vendidos:                         |\n";
        vector<pair<string,int>> ranking(contagemVendas_.begin(), contagemVendas_.end());
        sort(ranking.begin(), ranking.end(),
             [](const auto& a, const auto& b){ return a.second > b.second; });
        for (int i = 0; i < min((int)ranking.size(), 5); i++)
            cout << "  |   " << left << setw(28) << ranking[i].first
                 << right << setw(4) << ranking[i].second << " venda(s)  |\n";
        cout << "  +----------------------------------------------+\n\n";
    }

private:
    string nome_;
    vector<Jogo*>    catalogo_;
    map<string, Usuario> usuarios_;
    vector<Recibo>   recibos_;
    map<string, int> contagemVendas_;

    void registrarVenda(const vector<ItemCarrinho>& itens) {
        for (const auto& item : itens)
            contagemVendas_[item.getJogo()->getTitulo()]++;
    }
};

// ─────────────────────────────────────────
//  DEMO
// ─────────────────────────────────────────
int main() {
    cout << "\n" << string(52, '=') << "\n";
    cout << "  EstreamG -- Simulador de Loja de EGames\n";
    cout << string(52, '=') << "\n";

    Loja loja("EstreamG");

    // Jogos (alocados no heap para simplificar ownership)
    Jogo eldenRing  ("Elden Ring",       "FromSoftware", 199.90, "RPG");
    Jogo cs2        ("CS2",              "Valve",           0.0, "FPS");
    Jogo civ7       ("Civilization VII", "Firaxis",       249.90, "Estrategia");
    Jogo hollowKnight("Hollow Knight",   "Team Cherry",    37.99, "RPG");
    Jogo celeste    ("Celeste",          "Maddy Thorson",  19.99, "Plataforma");

    cout << "\n-- Cadastrando jogos --\n";
    loja.cadastrarJogo(&eldenRing);
    loja.cadastrarJogo(&cs2);
    loja.cadastrarJogo(&civ7);
    loja.cadastrarJogo(&hollowKnight);
    loja.cadastrarJogo(&celeste);

    cout << "\n-- Cadastrando usuarios --\n";
    loja.cadastrarUsuario("Lucas",  "lucas@email.com",  "senha123");
    loja.cadastrarUsuario("Camila", "camila@email.com", "outrasenha");

    cout << "\n-- Login --\n";
    Usuario* lucas = loja.login("lucas@email.com", "senha123");
    loja.login("lucas@email.com", "errada");

    loja.listarCatalogo();
    loja.buscarPorCategoria("RPG");

    cout << "\n-- Adicionando ao carrinho --\n";
    lucas->depositarSaldo(500.0);
    lucas->adicionarAoCarrinho(&eldenRing);
    lucas->adicionarAoCarrinho(&eldenRing);   // duplicata
    lucas->adicionarAoCarrinho(&civ7);
    lucas->adicionarAoCarrinho(&cs2);

    Cupom cupomRpg  ("RPG20",   20.0, {2027, 12, 31}, "RPG");
    Cupom cupomGeral("SAVE10",  10.0, {2027, 12, 31});

    cout << "\n-- Aplicando cupons --\n";
    lucas->aplicarCupom("Elden Ring",       &cupomRpg);
    lucas->aplicarCupom("Civilization VII", &cupomRpg);   // categoria errada
    lucas->aplicarCupom("CS2",              &cupomGeral);

    lucas->verCarrinho();

    cout << "\n-- Finalizando compra --\n";
    Recibo* rec1 = loja.finalizarCompra(lucas);
    if (rec1) rec1->exibir();

    lucas->verBiblioteca();
    lucas->registrarHoras("Elden Ring", 12.5);
    lucas->registrarHoras("CS2", 5.0);
    lucas->verBiblioteca();

    cout << "\n-- Avaliacoes --\n";
    loja.avaliarJogo("Elden Ring",       5, lucas);
    loja.avaliarJogo("Civilization VII", 4, lucas);
    loja.avaliarJogo("Hollow Knight",    5, lucas);  // nao possui

    cout << "\n-- Segunda compra (Camila) --\n";
    Usuario* camila = loja.login("camila@email.com", "outrasenha");
    camila->depositarSaldo(100.0);
    camila->adicionarAoCarrinho(&hollowKnight);
    camila->adicionarAoCarrinho(&celeste);
    Recibo* rec2 = loja.finalizarCompra(camila);
    if (rec2) rec2->exibir();

    loja.relatorioVendas();
    loja.listarCatalogo();

    return 0;
}
