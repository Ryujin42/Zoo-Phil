from specie import Specie
from enclosure import Enclosure


class Animal:
    def __init__(self, id: int, name: str, species: Specie, age: int, enclosure: Enclosure):
        self.id = id
        self.name = name
        self.species = species
        self.age = age
        self.enclosure = enclosure

    def __str__(self):
        return f'{self.name} animal'
