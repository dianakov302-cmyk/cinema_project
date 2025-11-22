from person import Person

class Actor(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_role(self):
        return "actor"

    def __str__(self):
        return f"{super().__str__()} — актор"
