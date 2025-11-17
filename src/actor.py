from person import Person

# 🔸 Наслідування: клас Actor успадковує все від Person
class Actor(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

    # 🔸 Поліморфізм: реалізуємо метод get_role() по-своєму
    def get_role(self):
        return "actor"

    def __str__(self):
        return f"{super().__str__()} — актор"
