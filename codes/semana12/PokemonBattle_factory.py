from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass, field


# ── Produto base ──────────────────────────────────────────
@dataclass
class Pokemon(ABC):
    name:   str
    hp:     int
    attack: int

    @abstractmethod
    def use_move(self) -> None: ...

    def status(self) -> str:
        return (f"{self.name:<14}"
                f"HP:{self.hp:>4}  "
                f"ATK:{self.attack:>4}")


# ── Produtos concretos ────────────────────────────────────
class FirePokemon(Pokemon):
    def use_move(self) -> None:
        print(f"{self.name} usou LANÇA-CHAMAS! "
              f"(dano base: {self.attack})")

class WaterPokemon(Pokemon):
    def use_move(self) -> None:
        print(f"{self.name} usou HIDROBOMBA! "
              f"(dano base: {self.attack})")

class GrassPokemon(Pokemon):
    def use_move(self) -> None:
        print(f"{self.name} usou FOLHA-NAVALHA! "
              f"(dano base: {self.attack})")

class PsychicPokemon(Pokemon):
    def use_move(self) -> None:
        print(f"{self.name} usou PSIQUICO! "
              f"(dano base: {self.attack})")


# ── Simple Factory com registry ───────────────────────────
class PokemonFactory:
    _registry: dict[str, type[Pokemon]] = {
        "fire":    FirePokemon,
        "water":   WaterPokemon,
        "grass":   GrassPokemon,
        "psychic": PsychicPokemon,
    }

    @classmethod
    def catch(
        cls,
        poke_type: str,
        name: str,
        hp: int,
        attack: int,
    ) -> Pokemon:
        if poke_type not in cls._registry:
            raise ValueError(
                f"Tipo {poke_type!r} nao existe na Pokedex!")
        return cls._registry[poke_type](
            name=name, hp=hp, attack=attack)

    @classmethod
    def register(
        cls,
        poke_type: str,
        klass: type[Pokemon],
    ) -> None:
        """Adiciona novo tipo sem alterar codigo existente."""
        cls._registry[poke_type] = klass


# ── Uso ───────────────────────────────────────────────────
if __name__ == "__main__":
    team_data = [
        ("fire",    "Charizard",  78, 84),
        ("water",   "Blastoise",  79, 83),
        ("grass",   "Venusaur",   80, 82),
        ("psychic", "Mewtwo",    106, 110),
    ]

    print("=== Status do Time ===")
    team = [PokemonFactory.catch(*d) for d in team_data]
    for p in team:
        print(p.status())

    print("=== Batalha! ===")
    for p in team:
        p.use_move()

    # Extensao dinamica — novo tipo sem alterar a factory
    class DragonPokemon(Pokemon):
        def use_move(self) -> None:
            print(f"{self.name} usou PULSO-DRAGAO! "
                  f"(dano base: {self.attack})")

    PokemonFactory.register("dragon", DragonPokemon)
    dragonite = PokemonFactory.catch(
        "dragon", "Dragonite", hp=91, attack=134)

    print("=== Novo tipo registrado ===")
    print(dragonite.status())
    dragonite.use_move()

    # Tipo invalido
    try:
        PokemonFactory.catch("electric", "Pikachu", 35, 55)
    except ValueError as e:
        print(f"Erro: {e}")