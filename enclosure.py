class Enclosure:
    def __init__(self, id: int, name: str, size: str, allowed_species: list[int]):
        self.enclosure_id = id
        self.name = name
        self.size = size
        self.allowed_species = allowed_species
        self.animals = []

    def add_animal(self, animal):
        if animal.specie_id in self.allowed_species:
            self.animals.append(animal)
            animal.enclosure_id = self.enclosure_id
        else:
            raise ValueError("This species is not allowed in this enclosure.")

    def remove_animal(self, animal):
        if animal in self.animals:
            self.animals.remove(animal)
            animal.enclosure_id = None
        else:
            raise ValueError("This animal is not in this enclosure.")

    def is_empty(self):
        return len(self.animals) == 0
