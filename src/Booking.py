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