from actor import Actor
from director import Director
from movie import Movie
from genre import Genre

# Створюємо об’єкти
actor1 = Actor("Емма Стоун", 35)
actor2 = Actor("Раян Гослінг", 44)
director1 = Director("Демієн Шазелл", 39, "мюзикл")
genre1 = Genre("Мюзикл")

# Створюємо фільм
movie1 = Movie("Ла-ла Ленд", 2016, director1, genre1)
movie1.add_actor(actor1)
movie1.add_actor(actor2)

# Виводимо все
print(movie1)



