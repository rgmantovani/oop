from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, field


# ── Produto base ─────────────────────────────────────────
@dataclass
class Tool(ABC):
    _max_durability: int = field(init=False)
    _durability: int     = field(init=False)

    def __post_init__(self) -> None:
        self._max_durability = self._base_durability()
        self._durability     = self._max_durability

    @abstractmethod
    def _base_durability(self) -> int: ...

    @property
    @abstractmethod
    def name(self) -> str: ...

    @property
    @abstractmethod
    def damage(self) -> int: ...

    @property
    def durability(self) -> int:
        return self._durability

    def use(self) -> None:
        if self._durability > 0:
            self._durability -= 1

    def is_broken(self) -> bool:
        return self._durability <= 0

    def show_info(self) -> None:
        print(f"{self.name:<14} dur: {self._durability:>4}  "
              f"dmg: {self.damage}")


# ── Produtos concretos ───────────────────────────────────
class WoodSword(Tool):
    name   = "WoodSword"
    damage = 4
    def _base_durability(self) -> int: return 60

class StoneSword(Tool):
    name   = "StoneSword"
    damage = 5
    def _base_durability(self) -> int: return 132

class IronSword(Tool):
    name   = "IronSword"
    damage = 6
    def _base_durability(self) -> int: return 251

class DiamondSword(Tool):
    name   = "DiamondSword"
    damage = 7
    def _base_durability(self) -> int: return 1562


# ── Simple Factory com registro dinâmico ─────────────────
class ToolFactory:
    _registry: dict[str, type[Tool]] = {
        "wood":    WoodSword,
        "stone":   StoneSword,
        "iron":    IronSword,
        "diamond": DiamondSword,
    }

    @classmethod
    def craft(cls, material: str) -> Tool:
        if material not in cls._registry:
            raise ValueError(
                f"Material desconhecido: {material!r}")
        return cls._registry[material]()

    @classmethod
    def register(cls, name: str, klass: type[Tool]) -> None:
        """Extensão sem alterar código existente (OCP)."""
        cls._registry[name] = klass


# ── Simulação de combate (Bônus) ─────────────────────────
def simulate_combat(tool: Tool) -> None:
    hits = 0
    while not tool.is_broken():
        tool.use()
        hits += 1
    print(f"{tool.name} quebrou após {hits} golpes!")


# ── Uso ──────────────────────────────────────────────────
if __name__ == "__main__":
    
    print("=== Inventário ===")
    for mat in ["wood", "stone", "iron", "diamond"]:
        ToolFactory.craft(mat).show_info()

    # Bônus: combate
    print("\n=== Combate ===")
    simulate_combat(ToolFactory.craft("wood"))

    # Tipo inválido → exceção
    try:
        ToolFactory.craft("gold")
    except ValueError as e:
        print(f"Erro: {e}")

    # Extensão dinâmica (OCP)
    class NetheriteSword(Tool):
        name   = "NetheriteSword"
        damage = 8
        def _base_durability(self) -> int: return 2031

    ToolFactory.register("netherite", NetheriteSword)
    ToolFactory.craft("netherite").show_info()