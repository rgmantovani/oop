import numpy as np 

class Pilha:
    # construtor
    def __init__(self, N = 8):
        #aqui dentro
        self.__topo = -1
        self.__vetor = np.zeros(N, dtype=int)
        self.__N = N

    def imprimePilha(self):
        print(self.__vetor)
    
    # retornar o topo
    def getTopo(self):
        return self.__topo
    
    def estaVazia(self):
        return (self.__topo == -1) 
    
    def estaCheia(self):
        return (self.__topo == self.__N-1)

    # empilhar
    def empilhar(self, valor):
        if not self.estaCheia():
            self.__topo += 1
            self.__vetor[self.__topo] = valor

    # desempilhar
    def desempilhar(self):
        aux = None
        if not self.estaVazia():
            aux = self.vetor[self.__topo]
            self.__topo -= 1
        return (aux)

if __name__ == "__main__":
    
    pilha = Pilha(3)
    print(pilha.estaVazia())
    print(pilha.estaCheia())
    pilha.imprimePilha()

    pilha.empilhar(36)
    # pilha.imprimePilha()
    pilha.empilhar(7)
    # pilha.imprimePilha()
    pilha.empilhar(9)
    # pilha.imprimePilha()
    pilha.empilhar(53)
    pilha.imprimePilha()

    pilha2 = Pilha(10)
    pilha2.imprimePilha()
    
    