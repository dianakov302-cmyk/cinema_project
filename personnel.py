from abc import ABC, abstractmethod

class Personnel(ABC):
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def info(self):
        return f'{self.name} працює як {self.position}. Зарплата: {self.salary} грн.'

    @abstractmethod
    def do_something(self):
        pass

class cashier(Personnel):
    def __init__(self, name, salary):
        super().__init__(name, 'Касир', salary)
        self.sold_tickets = 0

    def do_something(self):
        return f'{self.name} продає квитки.'

    def sell_tickets(self, number):
        self.sold_tickets += number
        return f'{self.name} продав {number} квитків. Всьго продано: {self.sold_tickets}.'

class Buffet(Personnel):
    def __init__(self, name, salary):
        super().__init__(name, 'Працівник Буфету', salary)
        self.sold_goods = 0

    def do_something(self):
        return f'{self.name} готує попкорн і продає напої у буфеті.'


    def sell_goods(self, number):
        self.sold_goods += number
        return f'{self.name} продав {number} товарів. Всього: {self.sold_goods}.'


class Manager(Personnel):
    def __init__(self, name, salary):
        super().__init__(name, "Менеджер", salary)
        self.subordinates = []  # список підлеглих працівників

    def add_personnel(self, person):
        self.subordinates.append(person)
        return f"{person.name} тепер під керівництвом {self.name}."

    def do_something(self):
        return f"{self.name} керує персоналом та контролює роботу касира і буфету."

    def show_team(self):
        if not self.subordinates:
            return f"{self.name} наразі не має підлеглих."
        team = ", ".join([p.name for p in self.subordinates])
        return f"{self.name} керує такими працівниками: {team}."


cashier1 = cashier('Олег', 15000)
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

