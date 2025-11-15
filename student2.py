class Review:
    """Клас для представлення відгуку."""

    def __init__(self, user_name, movie_title, rating, comment):
        self.user_name = user_name
        self.movie_title = movie_title
        self.rating = rating
        self.comment = comment

    def edit_review(self, new_rating, new_comment):
        """Редагує відгук."""
        self.rating = new_rating
        self.comment = new_comment

    def __str__(self):
        return f"⭐ {self.user_name} про '{self.movie_title}': {self.rating}/5 — {self.comment}"


class Hall:
    def __init__(self, hall_id, name, seats_count):
        self.hall_id = hall_id
        self.name = name
        self.seats_count = seats_count
        self.seats = []

    def add_seat(self, seat: Seat):

        if len(self.seats) < self.seats_count:
            self.seats.append(seat)
        else:
            print("❌ Неможливо додати більше місць!")

    def get_free_seats(self):
        return [seat for seat in self.seats if not seat.is_taken]

    def __str__(self):
        return f"Зал {self.name} (ID: {self.hall_id}, місць: {self.seats_count})"


class Seat:
    """Клас для представлення місця у залі."""

    def __init__(self, row, number, is_vip=False):
        self.row = row  # ряд
        self.number = number  # номер місця
        self.is_vip = is_vip  # чи VIP
        self.is_taken = False  # чи зайняте

    def book(self):
        """Бронює місце."""
        if not self.is_taken:
            self.is_taken = True
            print(f"✅ Місце {self.row}-{self.number} заброньовано.")
        else:
            print("❌ Це місце вже зайняте!")

    def cancel_booking(self):
        """Скасовує бронювання."""
        if self.is_taken:
            self.is_taken = False
            print(f"🔓 Місце {self.row}-{self.number} знову вільне.")
        else:
            print("ℹ️ Це місце і так вільне.")

    def __str__(self):
        vip = " (VIP)" if self.is_vip else ""
        status = "Зайняте" if self.is_taken else "Вільне"
        return f"Місце {self.row}-{self.number}{vip} — {status}"


from datetime import datetime


class Session:
    """Клас для представлення сеансу."""

    def __init__(self, session_id, movie_title, hall, start_time, price):
        self.session_id = session_id
        self.movie_title = movie_title
        self.hall = hall
        self.start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M")
        self.price = price

    def change_price(self, new_price):
        """Змінює ціну на квиток."""
        self.price = new_price

    def __str__(self):
        time_str = self.start_time.strftime("%Y-%m-%d %H:%M")
        return f"🎬 Сеанс '{self.movie_title}' — {time_str}, зал: {self.hall.name}, ціна: {self.price} грн"