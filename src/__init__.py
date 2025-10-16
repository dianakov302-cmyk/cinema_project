def person():
    return None
class Movie:
    def __init__(self, title, year, director=None, actors=None, genres=None, rating=0.0):
        self.title = title
        self.year = year
        self.director = director
        self.actors = actors if actors is not None else []
        self.genres = genres if genres is not None else []
        self.rating = rating
