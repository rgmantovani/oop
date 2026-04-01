import copy

class CreateAndDestroy:

    def __init__(self, name):
        self.__name = name
        print(f"Object {self.__name} created.")
    
    def __del__(self):
        print(f"Object {self.__name} destroyed.")

    def setName(self, name):
        self.__name = name

    def getName(self):
        return(self.__name)
    

if __name__ == "__main__":

    # Creating objects
    obj1 = CreateAndDestroy("1")
    obj2 = CreateAndDestroy("2")
    
    # Cuidado, copia a referencia (similar a um ponteiro)
    obj3 = obj2
    obj3.setName("3")

    # cria uma copia do objeto
    obj4 = copy.copy(obj1)
    obj4.setName("4")

    # Deleting objects (destruction happens automatically)
    del obj1 
    del obj2
    #del obj3
    del obj4