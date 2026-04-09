class Dog:

    def __init__(self, name="Toto"):
        self.name = name
        self.tricks = []
    
    def add_trick(self, trick):
        self.tricks.append(trick)


if __name__ == "__main__":

    d = Dog("Fido")
    e = Dog("Buddy")
    f = Dog()


    d.add_trick('roll over')
    e.add_trick('play dead')
    f.add_trick('bite flipflops')

    print(d.name)
    print(d.tricks)
    print(e.name)
    print(e.tricks)
    print(f.name)
    print(f.tricks)

