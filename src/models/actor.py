from models.person import Person
class Actor(Person):
    def __init__(self, name, age, movies = None):
        super().__init__(name, age)
        self.movies = movies if movies is not None else []

    def get_role(self):
            return 'actor'
    def add_movies(self, movie_title):
            self.movies.append(movie_title)
    def __str__(self):
            return f"{super().__str__()} — актор. Фільми: {', '.join(self.movies) if self.movies else 'немає'}"
