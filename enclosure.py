class Enclosure:
    def __init__(self, id: int, name: str, size: str, allowed_species: list[str]) -> None:
        self.enclosure_id = id
        self.name = name
        self.size = size
        self.allowed_species = allowed_species
        self.animals = []

    def add_animal(self, animal) -> None:
        if animal.specie not in self.allowed_species:
            raise ValueError("This species is not allowed in this enclosure.")

        self.animals.append(animal)
        animal.enclosure_id = self.enclosure_id

    def remove_animal(self, animal) -> None:
        if animal not in self.animals:
            raise ValueError("This animal is not in this enclosure.")

        self.animals.remove(animal)
        animal.enclosure_id = None

    def is_empty(self) -> bool:
        return len(self.animals) == 0
