class Client:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"Клієнт: {self.name}, Email: {self.email}, Телефон: {self.phone}"
