from actor import Actor
from director import Director
from movie import Movie
from genre import Genre


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



