from actor import Actor
from director import Director
from genre import Genre

# 🔸 Клас Movie об’єднує всі попередні — композиція (інший принцип, додатковий до ООП)
class Movie:
    def __init__(self, title, year, director: Director, genre: Genre, actors=None):
        self.title = title
        self.year = year
        self.director = director
        self.genre = genre
        self.actors = actors if actors else []

    # 🔸 Метод (поведінка об'єкта): додає актора у фільм
    def add_actor(self, actor: Actor):
        self.actors.append(actor)

    def __str__(self):
        actor_names = ', '.join([a.name for a in self.actors]) if self.actors else 'немає акторів'
        return (f"🎬 '{self.title}' ({self.year})\n"
                f"Жанр: {self.genre.name}\n"
                f"Режисер: {self.director.name}\n"
                f"Актори: {actor_names}")
