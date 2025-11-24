from actor import Actor
from director import Director
from movie import Movie
from genre import Genre
from personnel import Cashier, Buffet, Manager
from student2 import Review, Seat, Hall, Session




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

print(hall1)
for seat in hall1.seats:
    print(seat)

print(session1)
print(review1)



