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
