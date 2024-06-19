from specie import Specie


class Enclosure:
    def __init__(self, id: int, name: str, size: int, species: list[Specie]):
        self.id = id
        self.name = name
        self.size = size

    def __str__(self):
        return f'{self.name} enclosure'
