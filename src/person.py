from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 🔸 Поліморфізм: метод get_role() буде реалізований по-різному в Actor і Director
    @abstractmethod
    def get_role(self):
        pass

    def __str__(self):
        return f"{self.name}, {self.age} років"



from person import Person

class Actor(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_role(self):
        return "actor"

    def __str__(self):
        return f"{super().__str__()} — актор"

    from person import Person

    # 🔸 Наслідування: Director — теж Person, але з власною властивістю style
class Director(Person):
        def __init__(self, name, age, style):
            super().__init__(name, age)
            self.style = style  # 🔸 Інкапсуляція: зберігаємо особистий стиль режисера

        def get_role(self):
            return "director"

        def __str__(self):
            return f"{super().__str__()} — режисер у стилі {self.style}"











class Genre:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Жанр: {self.name}"






class Movie:
    def __init__(self, title, year, director: Director, genre: Genre, actors=None):
        self.title = title
        self.year = year
        self.director = director
        self.genre = genre
        self.actors = actors if actors else []

    def add_actor(self, actor: Actor):
        self.actors.append(actor)

    def __str__(self):
        actor_names = ', '.join([a.name for a in self.actors]) if self.actors else 'немає акторів'
        return (f"🎬 '{self.title}' ({self.year})\n"
                f"Жанр: {self.genre.name}\n"
                f"Режисер: {self.director.name}\n"
                f"Актори: {actor_names}")
