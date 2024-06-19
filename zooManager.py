class ZooManager:
    def __init__(self):
        self.animals = {}
        self.enclosures = {}
        self.visits = {}

    def add_animal(self, animal):
        self.animals[animal.animal_id] = animal

    def modify_animal(self, animal_id, **kwargs):
        if animal_id in self.animals:
            animal = self.animals[animal_id]
            for key, value in kwargs.items():
                setattr(animal, key, value)
        else:
            raise ValueError("Animal not found.")

    def remove_animal(self, animal_id):
        if animal_id in self.animals:
            del self.animals[animal_id]
        else:
            raise ValueError("Animal not found.")

    def add_enclosure(self, enclosure):
        self.enclosures[enclosure.enclosure_id] = enclosure

    def modify_enclosure(self, enclosure_id, **kwargs):
        if enclosure_id in self.enclosures:
            enclosure = self.enclosures[enclosure_id]
            for key, value in kwargs.items():
                setattr(enclosure, key, value)
        else:
            raise ValueError("Enclosure not found.")

    def remove_enclosure(self, enclosure_id):
        if enclosure_id in self.enclosures:
            enclosure = self.enclosures[enclosure_id]
            if enclosure.is_empty():
                del self.enclosures[enclosure_id]
            else:
                raise ValueError("Enclosure is not empty.")
        else:
            raise ValueError("Enclosure not found.")

    def add_visit(self, visit):
        self.visits[visit.visit_id] = visit

    def modify_visit(self, visit_id, **kwargs):
        if visit_id in self.visits:
            visit = self.visits[visit_id]
            for key, value in kwargs.items():
                setattr(visit, key, value)
        else:
            raise ValueError("Visit not found.")

    def remove_visit(self, visit_id):
        if visit_id in self.visits:
            del self.visits[visit_id]
        else:
            raise ValueError("Visit not found.")
