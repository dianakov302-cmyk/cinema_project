from person import Person

class Director(Person):
    def __init__(self, name, age, style):
        super().__init__(name, age)
        self.style = style
    def get_role(self):
            return 'director'
    def __str__(self):
            return f"{super().__str__()} — режисер у стилі {self.style}"
