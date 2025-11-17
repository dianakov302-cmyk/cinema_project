from person import Person

# 🔸 Наслідування: Director — теж Person, але з власною властивістю style
class Director(Person):
    def __init__(self, name, age, style):
        super().__init__(name, age)
        self.style = style  # 🔸 Інкапсуляція: зберігаємо особистий стиль режисера

    # 🔸 Поліморфізм: реалізація get_role() для режисера
    def get_role(self):
        return "director"

    def __str__(self):
        return f"{super().__str__()} — режисер у стилі {self.style}"
