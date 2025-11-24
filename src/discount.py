class Discount:
    def __init__(self, discount_type, percent):
        self.discount_type = discount_type  # тип знижки (студентська, постійний клієнт)
        self.percent = percent               # відсоток знижки

    def apply_discount(self, price):
        """Повертає ціну після застосування знижки"""
        return price * (1 - self.percent / 100)

    def __str__(self):
        return f"Знижка: {self.discount_type} ({self.percent}%)"