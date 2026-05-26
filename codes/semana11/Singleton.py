class Singleton:

    _instance = None

    def __init__(self, name: str):
        self.name = name

    @classmethod
    def Instance(cls):
        if cls._instance is None:
            cls._instance = Singleton("unico")
        return cls._instance

    def getName(self) -> str:
        return self.name


if __name__ == "__main__":
    a = Singleton.Instance()
    b = Singleton.Instance()
    c = Singleton.Instance()
    d = Singleton.Instance()

    print(f"nome de A: {a.getName()}")
    print(f"nome de B: {b.getName()}")
    print(f"nome de C: {c.getName()}")
    print(f"nome de D: {d.getName()}")
