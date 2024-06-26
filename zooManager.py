class ZooManager:
    def __init__(self):
        self.animals = {}
        self.enclosures = {}
        self.visits = {}

    def add_animal(self, animal):
        self.animals[animal.animal_id] = animal

    def modify_animal(self, animal_id, **kwargs):
        if animal_id not in self.animals:
            raise ValueError("Animal not found.")

        animal = self.animals[animal_id]
        for key, value in kwargs.items():
            setattr(animal, key, value)

    def remove_animal(self, animal_id):
        if animal_id not in self.animals:
            raise ValueError("Animal not found.")

        del self.animals[animal_id]

    def add_enclosure(self, enclosure):
        self.enclosures[enclosure.enclosure_id] = enclosure

    def modify_enclosure(self, enclosure_id, **kwargs):
        if enclosure_id not in self.enclosures:
            raise ValueError("Enclosure not found.")

        enclosure = self.enclosures[enclosure_id]
        for key, value in kwargs.items():
            setattr(enclosure, key, value)

    def remove_enclosure(self, enclosure_id):
        if enclosure_id not in self.enclosures:
            raise ValueError("Enclosure not found.")

        enclosure = self.enclosures[enclosure_id]
        if not enclosure.is_empty():
            raise ValueError("Enclosure is not empty.")

        del self.enclosures[enclosure_id]

    def add_visit(self, visit):
        self.visits[visit.visit_id] = visit

    def modify_visit(self, visit_id, **kwargs):
        if visit_id not in self.visits:
            raise ValueError("Visit not found.")

        visit = self.visits[visit_id]
        for key, value in kwargs.items():
            setattr(visit, key, value)

    def remove_visit(self, visit_id):
        if visit_id not in self.visits:
            raise ValueError("Visit not found.")

        del self.visits[visit_id]
