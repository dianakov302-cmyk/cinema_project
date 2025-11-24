from datetime import datetime

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


class Seat:
    """Клас для представлення місця у залі."""

    def __init__(self, row, number, is_vip=False):
        self.row = row
        self.number = number
        self.is_vip = is_vip
        self.is_taken = False

    def book(self):
        if not self.is_taken:
            self.is_taken = True
            print(f"✅ Місце {self.row}-{self.number} заброньовано.")
        else:
            print("❌ Це місце вже зайняте!")

    def cancel_booking(self):
        if self.is_taken:
            self.is_taken = False
            print(f"🔓 Місце {self.row}-{self.number} знову вільне.")
        else:
            print("ℹ️ Це місце і так вільне.")

    def __str__(self):
        vip = " (VIP)" if self.is_vip else ""
        status = "Зайняте" if self.is_taken else "Вільне"
        return f"Місце {self.row}-{self.number}{vip} — {status}"


class Hall:
    """Клас для представлення залу."""

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


class Session:
    """Клас для представлення сеансу."""

    def __init__(self, session_id, movie_title, hall, start_time, price):
        self.session_id = session_id
        self.movie_title = movie_title
        self.hall = hall
        self.start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M")
        self.price = price

    def change_price(self, new_price):
        self.price = new_price

    def __str__(self):
        time_str = self.start_time.strftime("%Y-%m-%d %H:%M")
        return f"🎬 Сеанс '{self.movie_title}' — {time_str}, зал: {self.hall.name}, ціна: {self.price} грн"


# ===========================
# Тестовий блок
# ===========================
if __name__ == "__main__":
    # Створюємо зал
    hall1 = Hall(1, "IMAX", 5)
    hall1.add_seat(Seat(1, 1))
    hall1.add_seat(Seat(1, 2, is_vip=True))
    hall1.add_seat(Seat(1, 3))

    # Створюємо сеанс
    session1 = Session(101, "Avatar 3", hall1, "2025-12-05 18:00", 250)

    # Створюємо відгук
    review1 = Review("Діана", "Avatar 3", 5, "Дуже крутий фільм!")

