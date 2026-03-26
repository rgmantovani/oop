"""
EstreamG — Simulador de Loja de EGames
Implementação em Python
"""

from datetime import date, datetime
import hashlib


# ─────────────────────────────────────────
#  JOGO
# ─────────────────────────────────────────
class Jogo:
    def __init__(self, titulo: str, desenvolvedor: str, preco: float, categoria: str):
        self.__titulo = titulo
        self.__desenvolvedor = desenvolvedor
        self.__preco = preco
        self.__categoria = categoria
        self.__avaliacoes: list[int] = []
        self.__ativo = True

    # ── getters ──────────────────────────
    def get_titulo(self) -> str:
        return self.__titulo

    def get_preco(self) -> float:
        return self.__preco

    def get_categoria(self) -> str:
        return self.__categoria

    def get_desenvolvedor(self) -> str:
        return self.__desenvolvedor

    # ── avaliações ───────────────────────
    def avaliar(self, nota: int) -> bool:
        if not self.__validar_nota(nota):
            print(f"  [!] Nota inválida. Use um inteiro entre 1 e 5.")
            return False
        self.__avaliacoes.append(nota)
        return True

    def media_avaliacoes(self):
        if not self.__avaliacoes:
            return "Sem avaliações"
        return round(sum(self.__avaliacoes) / len(self.__avaliacoes), 1)

    # ── estado ───────────────────────────
    def desativar(self):
        self.__ativo = False

    def esta_ativo(self) -> bool:
        return self.__ativo

    # ── privado ──────────────────────────
    def __validar_nota(self, nota) -> bool:
        return isinstance(nota, int) and 1 <= nota <= 5

    def __str__(self):
        return (f"{self.__titulo} | {self.__categoria} | "
                f"R$ {self.__preco:.2f} | ★ {self.media_avaliacoes()}")


# ─────────────────────────────────────────
#  CUPOM
# ─────────────────────────────────────────
class Cupom:
    def __init__(self, codigo: str, percentual: float,
                 validade: date, categoria_restrita: str = None,
                 uso_unico: bool = True):
        self.__codigo = codigo
        self.__percentual_desconto = percentual
        self.__data_validade = validade
        self.__categoria_restrita = categoria_restrita
        self.__uso_unico = uso_unico
        self.__usado = False

    def get_codigo(self) -> str:
        return self.__codigo

    def get_desconto(self) -> float:
        return self.__percentual_desconto

    def get_categoria_restrita(self):
        return self.__categoria_restrita

    def esta_valido(self) -> bool:
        vencido = date.today() > self.__data_validade
        ja_usado = self.__uso_unico and self.__usado
        return not vencido and not ja_usado

    def aplicavel_ao_jogo(self, jogo: Jogo) -> bool:
        if self.__categoria_restrita is None:
            return True
        return jogo.get_categoria() == self.__categoria_restrita

    def consumir(self) -> bool:
        if not self.esta_valido():
            print(f"  [!] Cupom '{self.__codigo}' inválido ou já utilizado.")
            return False
        self.__usado = True
        return True


# ─────────────────────────────────────────
#  ITEM CARRINHO
# ─────────────────────────────────────────
class ItemCarrinho:
    def __init__(self, jogo: Jogo):
        self.__jogo = jogo
        self.__cupom_aplicado: Cupom | None = None

    def get_jogo(self) -> Jogo:
        return self.__jogo

    def get_quantidade(self) -> int:
        return 1  # jogos digitais: sempre 1 unidade

    def aplicar_cupom(self, cupom: Cupom) -> bool:
        if not cupom.esta_valido():
            print(f"  [!] Cupom '{cupom.get_codigo()}' está expirado ou já foi usado.")
            return False
        if not cupom.aplicavel_ao_jogo(self.__jogo):
            print(f"  [!] Cupom '{cupom.get_codigo()}' não é válido para "
                  f"jogos da categoria '{self.__jogo.get_categoria()}'.")
            return False
        self.__cupom_aplicado = cupom
        print(f"  [✓] Cupom '{cupom.get_codigo()}' aplicado em '{self.__jogo.get_titulo()}'.")
        return True

    def get_preco_final(self) -> float:
        if self.__cupom_aplicado:
            desconto = self.__jogo.get_preco() * (self.__cupom_aplicado.get_desconto() / 100)
            return round(self.__jogo.get_preco() - desconto, 2)
        return self.__jogo.get_preco()

    def get_desconto_aplicado(self) -> float:
        return round(self.__jogo.get_preco() - self.get_preco_final(), 2)

    def get_cupom(self):
        return self.__cupom_aplicado


# ─────────────────────────────────────────
#  CARRINHO
# ─────────────────────────────────────────
class Carrinho:
    def __init__(self, id_usuario: str):
        self.__itens: list[ItemCarrinho] = []
        self.__id_usuario = id_usuario

    def adicionar(self, jogo: Jogo) -> bool:
        if self.__buscar_item(jogo.get_titulo()):
            print(f"  [!] '{jogo.get_titulo()}' já está no carrinho.")
            return False
        self.__itens.append(ItemCarrinho(jogo))
        print(f"  [+] '{jogo.get_titulo()}' adicionado ao carrinho.")
        return True

    def remover(self, titulo: str) -> bool:
        item = self.__buscar_item(titulo)
        if not item:
            print(f"  [!] '{titulo}' não encontrado no carrinho.")
            return False
        self.__itens.remove(item)
        print(f"  [-] '{titulo}' removido do carrinho.")
        return True

    def aplicar_cupom_item(self, titulo: str, cupom: Cupom) -> bool:
        item = self.__buscar_item(titulo)
        if not item:
            print(f"  [!] '{titulo}' não está no carrinho.")
            return False
        return item.aplicar_cupom(cupom)

    def get_total(self) -> float:
        return round(sum(i.get_preco_final() for i in self.__itens), 2)

    def get_economia_total(self) -> float:
        return round(sum(i.get_desconto_aplicado() for i in self.__itens), 2)

    def listar(self):
        if not self.__itens:
            print("  Carrinho vazio.")
            return
        print("\n  ╔══════════════════════════════════════════════╗")
        print("  ║              🛒  CARRINHO                    ║")
        print("  ╠══════════════════════════════════════════════╣")
        for item in self.__itens:
            jogo = item.get_jogo()
            desconto = item.get_desconto_aplicado()
            print(f"  ║  {jogo.get_titulo():<28} R$ {jogo.get_preco():>7.2f}  ║")
            if desconto > 0:
                cupom = item.get_cupom()
                print(f"  ║    └─ Cupom {cupom.get_codigo()} (-{cupom.get_desconto():.0f}%)"
                      f"        -R$ {desconto:>6.2f}  ║")
        print("  ╠══════════════════════════════════════════════╣")
        economia = self.get_economia_total()
        if economia > 0:
            print(f"  ║  Economia total:              -R$ {economia:>9.2f}  ║")
        print(f"  ║  TOTAL:                        R$ {self.get_total():>9.2f}  ║")
        print("  ╚══════════════════════════════════════════════╝\n")

    def esta_vazio(self) -> bool:
        return len(self.__itens) == 0

    def get_itens(self) -> list[ItemCarrinho]:
        return list(self.__itens)  # cópia defensiva

    def limpar(self):
        self.__itens.clear()

    def __buscar_item(self, titulo: str):
        for item in self.__itens:
            if item.get_jogo().get_titulo() == titulo:
                return item
        return None


# ─────────────────────────────────────────
#  BIBLIOTECA
# ─────────────────────────────────────────
class Biblioteca:
    def __init__(self):
        self.__jogos_possuidos: list[str] = []
        self.__horas_jogadas: dict[str, float] = {}

    def adicionar_jogo(self, titulo: str) -> bool:
        if self.__jogo_na_biblioteca(titulo):
            return False
        self.__jogos_possuidos.append(titulo)
        self.__horas_jogadas[titulo] = 0.0
        return True

    def possui(self, titulo: str) -> bool:
        return self.__jogo_na_biblioteca(titulo)

    def registrar_horas(self, titulo: str, horas: float) -> bool:
        if not self.__jogo_na_biblioteca(titulo):
            print(f"  [!] '{titulo}' não está na sua biblioteca.")
            return False
        if horas <= 0:
            print("  [!] Horas devem ser positivas.")
            return False
        self.__horas_jogadas[titulo] += horas
        return True

    def get_horas(self, titulo: str) -> float:
        return self.__horas_jogadas.get(titulo, 0.0)

    def listar(self):
        if not self.__jogos_possuidos:
            print("  Biblioteca vazia.")
            return
        ordenados = sorted(self.__jogos_possuidos,
                           key=lambda t: self.__horas_jogadas.get(t, 0),
                           reverse=True)
        print("\n  ╔══════════════════════════════════════════════╗")
        print("  ║            🎮  MINHA BIBLIOTECA              ║")
        print("  ╠══════════════════════════════════════════════╣")
        for titulo in ordenados:
            horas = self.__horas_jogadas.get(titulo, 0.0)
            print(f"  ║  {titulo:<32} {horas:>6.1f}h  ║")
        print("  ╚══════════════════════════════════════════════╝\n")

    def __jogo_na_biblioteca(self, titulo: str) -> bool:
        return titulo in self.__jogos_possuidos


# ─────────────────────────────────────────
#  RECIBO
# ─────────────────────────────────────────
class Recibo:
    _contador = 1

    def __init__(self, usuario_nome: str, itens: list[ItemCarrinho]):
        self.__id_recibo = f"REC-{Recibo._contador:04d}"
        Recibo._contador += 1
        self.__usuario_nome = usuario_nome
        self.__itens_comprados = list(itens)
        self.__total_pago = round(sum(i.get_preco_final() for i in itens), 2)
        self.__total_economizado = round(sum(i.get_desconto_aplicado() for i in itens), 2)
        self.__data_hora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def exibir(self):
        print("\n  ╔══════════════════════════════════════════════╗")
        print(f"  ║  🧾  RECIBO {self.__id_recibo:<35}║")
        print(f"  ║  Data: {self.__data_hora:<39}║")
        print(f"  ║  Cliente: {self.__usuario_nome:<37}║")
        print("  ╠══════════════════════════════════════════════╣")
        for item in self.__itens_comprados:
            jogo = item.get_jogo()
            print(f"  ║  {jogo.get_titulo():<28} R$ {item.get_preco_final():>7.2f}  ║")
            if item.get_desconto_aplicado() > 0:
                print(f"  ║    └─ desconto aplicado      -R$ {item.get_desconto_aplicado():>7.2f}  ║")
        print("  ╠══════════════════════════════════════════════╣")
        if self.__total_economizado > 0:
            print(f"  ║  Você economizou:             R$ {self.__total_economizado:>9.2f}  ║")
        print(f"  ║  TOTAL PAGO:                  R$ {self.__total_pago:>9.2f}  ║")
        print("  ╚══════════════════════════════════════════════╝\n")

    def get_total_pago(self) -> float:
        return self.__total_pago

    def get_id(self) -> str:
        return self.__id_recibo


# ─────────────────────────────────────────
#  USUÁRIO
# ─────────────────────────────────────────
class Usuario:
    def __init__(self, nome: str, email: str, senha: str):
        self.__nome = nome
        self.__email = email
        self.__senha_hash = self.__hash_senha(senha)
        self.__saldo = 0.0
        self.__carrinho = Carrinho(email)
        self.__biblioteca = Biblioteca()
        self.__historico_recibos: list[Recibo] = []

    # ── getters ──────────────────────────
    def get_nome(self) -> str:
        return self.__nome

    def get_email(self) -> str:
        return self.__email

    def get_saldo(self) -> float:
        return self.__saldo

    # ── saldo ────────────────────────────
    def depositar_saldo(self, valor: float) -> bool:
        if valor <= 0:
            print("  [!] Valor de depósito deve ser positivo.")
            return False
        self.__saldo += valor
        print(f"  [✓] R$ {valor:.2f} depositado. Saldo atual: R$ {self.__saldo:.2f}")
        return True

    # ── carrinho ─────────────────────────
    def adicionar_ao_carrinho(self, jogo: Jogo) -> bool:
        if self.__biblioteca.possui(jogo.get_titulo()):
            print(f"  [!] Você já possui '{jogo.get_titulo()}' na biblioteca.")
            return False
        return self.__carrinho.adicionar(jogo)

    def remover_do_carrinho(self, titulo: str) -> bool:
        return self.__carrinho.remover(titulo)

    def aplicar_cupom(self, titulo: str, cupom: Cupom) -> bool:
        return self.__carrinho.aplicar_cupom_item(titulo, cupom)

    def ver_carrinho(self):
        self.__carrinho.listar()

    # ── biblioteca ───────────────────────
    def ver_biblioteca(self):
        self.__biblioteca.listar()

    def registrar_horas(self, titulo: str, horas: float) -> bool:
        return self.__biblioteca.registrar_horas(titulo, horas)

    # ── autenticação ─────────────────────
    def autenticar(self, senha: str) -> bool:
        return self.__hash_senha(senha) == self.__senha_hash

    # ── histórico ────────────────────────
    def adicionar_recibo(self, recibo: Recibo):
        self.__historico_recibos.append(recibo)

    def ver_historico(self):
        if not self.__historico_recibos:
            print("  Nenhuma compra realizada ainda.")
            return
        for recibo in self.__historico_recibos:
            recibo.exibir()

    # ── acesso interno para a Loja ───────
    def _get_carrinho(self) -> Carrinho:
        return self.__carrinho

    def _get_biblioteca(self) -> Biblioteca:
        return self.__biblioteca

    def _debitar_saldo(self, valor: float):
        self.__saldo -= valor

    # ── privados ─────────────────────────
    def __saldo_suficiente(self) -> bool:
        return self.__saldo >= self.__carrinho.get_total()

    def __hash_senha(self, senha: str) -> str:
        return hashlib.sha256(senha.encode()).hexdigest()


# ─────────────────────────────────────────
#  LOJA
# ─────────────────────────────────────────
class Loja:
    def __init__(self, nome: str = "EstreamG"):
        self.__nome = nome
        self.__catalogo: list[Jogo] = []
        self.__usuarios: dict[str, Usuario] = {}
        self.__recibos: list[Recibo] = []
        self.__contagem_vendas: dict[str, int] = {}

    # ── cadastros ────────────────────────
    def cadastrar_jogo(self, jogo: Jogo) -> bool:
        if self.__buscar_jogo(jogo.get_titulo()):
            print(f"  [!] Jogo '{jogo.get_titulo()}' já cadastrado.")
            return False
        self.__catalogo.append(jogo)
        print(f"  [✓] '{jogo.get_titulo()}' adicionado ao catálogo.")
        return True

    def cadastrar_usuario(self, nome: str, email: str, senha: str):
        if email in self.__usuarios:
            print(f"  [!] E-mail '{email}' já cadastrado.")
            return None
        usuario = Usuario(nome, email, senha)
        self.__usuarios[email] = usuario
        print(f"  [✓] Usuário '{nome}' cadastrado com sucesso.")
        return usuario

    # ── acesso ───────────────────────────
    def login(self, email: str, senha: str):
        usuario = self.__usuarios.get(email)
        if not usuario or not usuario.autenticar(senha):
            print("  [!] E-mail ou senha incorretos.")
            return None
        print(f"  [✓] Bem-vindo(a), {usuario.get_nome()}!")
        return usuario

    def buscar_jogo(self, titulo: str):
        jogo = self.__buscar_jogo(titulo)
        if not jogo:
            print(f"  [!] Jogo '{titulo}' não encontrado.")
        return jogo

    # ── catálogo ─────────────────────────
    def listar_catalogo(self):
        ativos = [j for j in self.__catalogo if j.esta_ativo()]
        if not ativos:
            print("  Catálogo vazio.")
            return
        print(f"\n  ╔══════════════════════════════════════════════════════╗")
        print(f"  ║           🎮  {self.__nome.upper()} — CATÁLOGO{'':>17}║")
        print(f"  ╠══════════════════════════════════════════════════════╣")
        for jogo in ativos:
            preco_str = "GRÁTIS" if jogo.get_preco() == 0 else f"R$ {jogo.get_preco():.2f}"
            print(f"  ║  {jogo.get_titulo():<26} {jogo.get_categoria():<12} "
                  f"{preco_str:>8}  ★ {jogo.media_avaliacoes()}  ║")
        print(f"  ╚══════════════════════════════════════════════════════╝\n")

    def buscar_por_categoria(self, categoria: str) -> list[Jogo]:
        resultado = [j for j in self.__catalogo
                     if j.get_categoria() == categoria and j.esta_ativo()]
        print(f"\n  Jogos na categoria '{categoria}': {len(resultado)} encontrado(s).")
        for j in resultado:
            print(f"    • {j}")
        return resultado

    # ── compra ───────────────────────────
    def finalizar_compra(self, usuario: Usuario):
        carrinho = usuario._get_carrinho()
        biblioteca = usuario._get_biblioteca()

        if carrinho.esta_vazio():
            print("  [!] Carrinho está vazio.")
            return None

        total = carrinho.get_total()

        if usuario.get_saldo() < total:
            print(f"  [!] Saldo insuficiente. "
                  f"Saldo: R$ {usuario.get_saldo():.2f} | Total: R$ {total:.2f}")
            return None

        # Verificação dupla: nenhum jogo já na biblioteca
        for item in carrinho.get_itens():
            titulo = item.get_jogo().get_titulo()
            if biblioteca.possui(titulo):
                print(f"  [!] '{titulo}' já está na sua biblioteca. Remova do carrinho.")
                return None

        # Consome cupons
        for item in carrinho.get_itens():
            cupom = item.get_cupom()
            if cupom:
                cupom.consumir()

        # Debita saldo
        usuario._debitar_saldo(total)

        # Adiciona à biblioteca
        itens = carrinho.get_itens()
        for item in itens:
            biblioteca.adicionar_jogo(item.get_jogo().get_titulo())

        # Registra vendas
        self.__registrar_venda(itens)

        # Gera recibo
        recibo = Recibo(usuario.get_nome(), itens)
        self.__recibos.append(recibo)
        usuario.adicionar_recibo(recibo)

        # Limpa carrinho
        carrinho.limpar()

        print(f"  [✓] Compra finalizada! "
              f"Saldo restante: R$ {usuario.get_saldo():.2f}")
        return recibo

    # ── avaliação ────────────────────────
    def avaliar_jogo(self, titulo: str, nota: int, usuario: Usuario) -> bool:
        if not usuario._get_biblioteca().possui(titulo):
            print(f"  [!] Você precisa possuir '{titulo}' para avaliá-lo.")
            return False
        jogo = self.__buscar_jogo(titulo)
        if not jogo:
            return False
        resultado = jogo.avaliar(nota)
        if resultado:
            print(f"  [✓] Avaliação {nota}★ registrada para '{titulo}'.")
        return resultado

    # ── relatório ────────────────────────
    def relatorio_vendas(self):
        print("\n  ╔══════════════════════════════════════════════╗")
        print("  ║          📊  RELATÓRIO DE VENDAS             ║")
        print("  ╠══════════════════════════════════════════════╣")
        total_arrecadado = sum(r.get_total_pago() for r in self.__recibos)
        print(f"  ║  Total de compras: {len(self.__recibos):<27}║")
        print(f"  ║  Total arrecadado: R$ {total_arrecadado:<23.2f}║")
        print("  ╠══════════════════════════════════════════════╣")
        print("  ║  Jogos mais vendidos:                        ║")
        ranking = sorted(self.__contagem_vendas.items(),
                         key=lambda x: x[1], reverse=True)
        for titulo, qtd in ranking[:5]:
            print(f"  ║    {titulo:<30} {qtd:>4} venda(s)  ║")
        print("  ╚══════════════════════════════════════════════╝\n")

    # ── privados ─────────────────────────
    def __buscar_jogo(self, titulo: str):
        for jogo in self.__catalogo:
            if jogo.get_titulo() == titulo:
                return jogo
        return None

    def __registrar_venda(self, itens: list[ItemCarrinho]):
        for item in itens:
            titulo = item.get_jogo().get_titulo()
            self.__contagem_vendas[titulo] = self.__contagem_vendas.get(titulo, 0) + 1


# ─────────────────────────────────────────
#  DEMO
# ─────────────────────────────────────────
if __name__ == "__main__":
    print("\n" + "═" * 52)
    print("  🎮  EstreamG — Simulador de Loja de EGames")
    print("═" * 52)

    loja = Loja("EstreamG")

    # ── Cadastro de jogos ──
    print("\n── Cadastrando jogos ──")
    loja.cadastrar_jogo(Jogo("Elden Ring",       "FromSoftware", 199.90, "RPG"))
    loja.cadastrar_jogo(Jogo("CS2",              "Valve",           0.0, "FPS"))
    loja.cadastrar_jogo(Jogo("Civilization VII", "Firaxis",       249.90, "Estratégia"))
    loja.cadastrar_jogo(Jogo("Hollow Knight",    "Team Cherry",    37.99, "RPG"))
    loja.cadastrar_jogo(Jogo("Celeste",          "Maddy Thorson",  19.99, "Plataforma"))

    # ── Cadastro de usuários ──
    print("\n── Cadastrando usuários ──")
    loja.cadastrar_usuario("Lucas",  "lucas@email.com",  "senha123")
    loja.cadastrar_usuario("Camila", "camila@email.com", "outrasenha")

    # ── Login ──
    print("\n── Login ──")
    lucas = loja.login("lucas@email.com", "senha123")
    loja.login("lucas@email.com", "errada")   # teste de senha errada

    # ── Catálogo ──
    loja.listar_catalogo()
    loja.buscar_por_categoria("RPG")

    # ── Compra com cupom ──
    print("\n── Adicionando jogos ao carrinho ──")
    lucas.depositar_saldo(500.0)
    lucas.adicionar_ao_carrinho(loja.buscar_jogo("Elden Ring"))
    lucas.adicionar_ao_carrinho(loja.buscar_jogo("Elden Ring"))   # duplicata
    lucas.adicionar_ao_carrinho(loja.buscar_jogo("Civilization VII"))
    lucas.adicionar_ao_carrinho(loja.buscar_jogo("CS2"))

    cupom_rpg  = Cupom("RPG20",  20.0, date(2027, 12, 31), categoria_restrita="RPG")
    cupom_geral = Cupom("SAVE10", 10.0, date(2027, 12, 31))

    print("\n── Aplicando cupons ──")
    lucas.aplicar_cupom("Elden Ring",       cupom_rpg)
    lucas.aplicar_cupom("Civilization VII", cupom_rpg)    # categoria errada
    lucas.aplicar_cupom("CS2",              cupom_geral)

    lucas.ver_carrinho()

    print("\n── Finalizando compra ──")
    recibo = loja.finalizar_compra(lucas)
    recibo.exibir()

    # ── Biblioteca e horas ──
    lucas.ver_biblioteca()
    lucas.registrar_horas("Elden Ring", 12.5)
    lucas.registrar_horas("CS2", 5.0)
    lucas.ver_biblioteca()

    # ── Avaliações ──
    print("\n── Avaliações ──")
    loja.avaliar_jogo("Elden Ring",       5, lucas)
    loja.avaliar_jogo("Civilization VII", 4, lucas)
    loja.avaliar_jogo("Hollow Knight",    5, lucas)  # não possui

    # ── Segunda compra ──
    print("\n── Segunda compra (Camila) ──")
    camila = loja.login("camila@email.com", "outrasenha")
    camila.depositar_saldo(100.0)
    camila.adicionar_ao_carrinho(loja.buscar_jogo("Hollow Knight"))
    camila.adicionar_ao_carrinho(loja.buscar_jogo("Celeste"))
    recibo2 = loja.finalizar_compra(camila)
    recibo2.exibir()

    # ── Relatório ──
    loja.relatorio_vendas()
    loja.listar_catalogo()
