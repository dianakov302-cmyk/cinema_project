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