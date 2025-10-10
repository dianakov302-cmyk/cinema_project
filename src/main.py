from models.actor import Actor
from models.director import Director

actor1 = Actor("Emma Stone", 35, ["La La Land", "Cruella"])
director1 = Director("Christopher Nolan", 54, "sci-fi")

print(actor1.get_role())      # → actor
print(director1.get_role())   # → director

print(actor1)                 # → Emma Stone, 35 років — актор. Фільми: La La Land, Cruella
print(director1)              # → Christopher Nolan, 54 років — режисер у стилі sci-fi
