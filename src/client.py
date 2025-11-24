class Client:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def __str__(self):
        return f"Клієнт: {self.name}, Email: {self.email}, Телефон: {self.phone}"
    # --- Клас Бронювання ---


class Booking:
    def __init__(self, client, ticket):
        self.client = client
        self.ticket = ticket
        self.is_confirmed = False

    def confirm_booking(self):
        self.is_confirmed = True
        print(f"✅ Бронювання підтверджено для {self.client.name} на фільм '{self.ticket.movie_title}'")

    def cancel_booking(self):
        self.is_confirmed = False
        print(f"❌ Бронювання скасовано для {self.client.name}")

    def __str__(self):
        status = "Підтверджено" if self.is_confirmed else "Очікує підтвердження"
        return f"{self.client.name} → {self.ticket.movie_title} ({status})"

    # --- Клас Квиток ---
class Ticket:
        def __init__(self, movie_title, seat, price, discount=None):
            self.movie_title = movie_title
            self.seat = seat
            self.price = price
            self.discount = discount

        def final_price(self):
            """Обчислює кінцеву ціну квитка з урахуванням знижки"""
            if self.discount:
                return self.discount.apply_discount(self.price)
            return self.price

        def __str__(self):
            return f"Квиток на '{self.movie_title}', місце {self.seat}, ціна: {self.final_price():.2f} грн"

class Discount:
            def __init__(self, discount_type, percent):
                self.discount_type = discount_type  # тип знижки (студентська, постійний клієнт)
                self.percent = percent  # відсоток знижки

            def apply_discount(self, price):
                """Повертає ціну після застосування знижки"""
                return price * (1 - self.percent / 100)

            def __str__(self):
                return f"Знижка: {self.discount_type} ({self.percent}%)"