from actor import Actor
from director import Director
from movie import Movie
from genre import Genre
from personnel import Cashier, Buffet, Manager
from student2 import Hall, Seat, Session, Review
# Імпорт класів
from client import Client
from booking import Booking
from discount import Discount
from ticket import Ticket






actor1 = Actor("Емма Стоун", 35)
actor2 = Actor("Раян Гослінг", 44)
actor3 = Actor("Вілл Сміт", 57)
actor4 = Actor("Леонардо Дікапріо", 51)
actor5 = Actor("Марго Роббі", 35)

director1 = Director("Демієн Шазелл", 39, "мюзикл")
director2 = Director("Грета Гервіг", 42, "сторі-тейлінг")
director3 = Director("Джон Рекуа", 58, "комедія")
director4 = Director("Адам Мак-Кей", 57, "реалістика")
director5 = Director("Крейг Гіллеспі", 39, "драма")

genre1 = Genre("Мюзикл")
genre2 = Genre("Фантастика")
genre3 = Genre("Фентезі")
genre4 = Genre("Комедія")
genre5 = Genre("Драма")


movie1 = Movie("Ла-ла Ленд", 2016, director1, genre1)
movie1.add_actor(actor1)
movie1.add_actor(actor2)

movie2 = Movie("Барбі", 2023, director2, genre3)
movie2.add_actor(actor5)
movie2.add_actor(actor2)

movie3 = Movie("Фокус", 2015, director3, genre4)
movie3.add_actor(actor3)
movie3.add_actor(actor5)

movie4 = Movie("Не дивіться в гору", 2020, director4, genre5)
movie4.add_actor(actor4)

movie5 = Movie("Круелла", 2021, director5, genre2)
movie5.add_actor(actor1)

print(movie1)
print(movie2)
print(movie3)
print(movie4)
print(movie5)



cashier1 = Cashier('Олег', 15000)
print(cashier1.info())
print(cashier1.do_something())
print(cashier1.sell_tickets(15))

print()


Buffet1 = Buffet('Ірина', 14000)
print(Buffet1.info())
print(Buffet1.do_something())
print(Buffet1.sell_goods(10))

print()

manager1 = Manager("Світлана", 20000)
print(manager1.info())
print(manager1.do_something())
print(manager1.add_personnel(cashier1))
print(manager1.add_personnel(Buffet1))
print(manager1.show_team())

# Імпорт класів з student2.py
from src.student2 import Review, Seat, Hall, Session

# -------------------------
# Створення об'єктів
# -------------------------
# Створюємо зал
hall1 = Hall(1, "IMAX", 5)
hall1.add_seat(Seat(1, 1))
hall1.add_seat(Seat(1, 2, is_vip=True))
hall1.add_seat(Seat(1, 3))
hall1.add_seat(Seat(1, 4))
hall1.add_seat(Seat(1, 5, is_vip=True))

# Створюємо сеанси
session1 = Session(101, "Avatar 3", hall1, "2025-12-05 18:00", 250)
session2 = Session(102, "Avatar 3", hall1, "2025-12-05 21:00", 300)

# Створюємо відгуки
review1 = Review("Діана", "Avatar 3", 5, "Дуже крутий фільм!")
review2 = Review("Іван", "Avatar 3", 4, "Добре, але трохи нуднувато.")

# -------------------------
# Вивід інформації
# -------------------------
print("=== Зал та місця ===")
print(hall1)
print("Вільні місця:")
for seat in hall1.get_free_seats():
    print(seat)
print()

print("=== Сеанси ===")
print(session1)
print(session2)
print()




print("=== Відгуки ===")
print(review1)
print(review2)
# ==========================
# Створення об'єктів
# ==========================
# Клієнти
client1 = Client("Діана", "diana@example.com", "+380671234567")
client2 = Client("Іван", "ivan@example.com", "+380671112233")

# Знижки
student_discount = Discount("Студентська", 15)
vip_discount = Discount("VIP", 20)

# Квитки
ticket1 = Ticket("Avatar 3", "A1", 250, discount=student_discount)
ticket2 = Ticket("Avatar 3", "A2", 250)
ticket3 = Ticket("Avatar 3", "A3", 250, discount=vip_discount)

# Бронювання
booking1 = Booking(client1, ticket1)
booking2 = Booking(client2, ticket2)
booking3 = Booking(client1, ticket3)

# Підтверджуємо бронювання
booking1.confirm_booking()
booking2.confirm_booking()
# booking3 залишимо не підтвердженим

# ==========================
# Вивід інформації
# ==========================
print("=== Клієнти ===")
print(client1)
print(client2)
print()

print("=== Квитки ===")
print(ticket1)
print(ticket2)
print(ticket3)
print()

print("=== Бронювання ===")
print(booking1)
print(booking2)
print(booking3)
print()

print("=== Знижки ===")
print(student_discount)
print(vip_discount)


