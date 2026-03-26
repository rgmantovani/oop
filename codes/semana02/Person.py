class Person:
    def __init__(self, age):
        self.age = age
        self.__name = "Default Name" # Another internal attribute managed directly

    @property
    def age(self):
        """The age property: retrieves the person's age."""
        return self._age

    @age.setter
    def age(self, value):
        """The age setter: validates and sets the person's age."""
        if not isinstance(value, int) or value < 0:
            raise ValueError("Age must be a non-negative integer")
        self._age = value

# --- Usage ---
if __name__ == "__main__":
   
    person = Person(30)
    print(f"Initial age: {person.age}")

    person.age = 35
    print(f"Modified age: {person.age}")

    # Attempt to set an invalid age (will raise ValueError)
    try:
        person.age = 15
        print(f"Modified age: {person.age}")
    except ValueError as e:
        print(f"Error: {e}")

    person.name = "John Doe"
    print (person.__name)
