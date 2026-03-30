class CreateAndDestoy:

    def __init__(self, name):
        self.name = name
        print(f"Object {self.name} created.")
    
    def __del__(self):
        print(f"Object {self.name} destroyed.")


if __name__ == "__main__":

    # Creating objects
    obj1 = CreateAndDestoy("1")
    obj2 = CreateAndDestoy("2")

    # Deleting objects (destruction happens automatically)
    del obj1 
    del obj2