import pytest

from datetime import datetime

from animal import Animal
from enclosure import Enclosure
from visit import Visit
from zooManager import ZooManager


# Tests pour la classe Animal
def test_animal_creation():
    animal = Animal(1, "Simba", "lion", 5, None)
    assert animal.animal_id == 1
    assert animal.name == "Simba"
    assert animal.specie == "lion"
    assert animal.age == 5
    assert animal.enclosure_id is None


# Tests pour la classe Enclosure
def test_enclosure_creation():
    enclosure = Enclosure(1, "Big Cats", "large", ["lion", "tiger"])
    assert enclosure.enclosure_id == 1
    assert enclosure.name == "Big Cats"
    assert enclosure.size == "large"
    assert enclosure.allowed_species == ["lion", "tiger"]
    assert enclosure.animals == []


def test_add_animal_to_enclosure():
    enclosure = Enclosure(1, "Big Cats", "large", ["lion", "tiger"])
    animal = Animal(1, "Simba", "lion", 5, None)
    enclosure.add_animal(animal)
    assert len(enclosure.animals) == 1
    assert enclosure.animals[0] == animal
    assert animal.enclosure_id == 1


def test_add_animal_to_invalid_enclosure():
    enclosure = Enclosure(1, "Big Cats", "large", ["lion", "tiger"])
    animal = Animal(1, "Nagini", "snake", 3, None)
    with pytest.raises(ValueError):
        enclosure.add_animal(animal)


def test_remove_animal_from_enclosure():
    enclosure = Enclosure(1, "Big Cats", "large", ["lion", "tiger"])
    animal = Animal(1, "Simba", "lion", 5, None)
    enclosure.add_animal(animal)
    enclosure.remove_animal(animal)
    assert len(enclosure.animals) == 0
    assert animal.enclosure_id is None


# Tests pour la classe Visit
def test_visit_creation():
    enclosure1 = Enclosure(1, "Big Cats", "large", ["lion", "tiger"])
    enclosure2 = Enclosure(2, "Reptile House", "medium", ["snake", "lizard"])
    visit = Visit(1, "2024-06-19", "10:00", "12:00", [enclosure1, enclosure2])
    assert visit.visit_id == 1
    assert visit.date == "2024-06-19"
    assert visit.start_time == "10:00"
    assert visit.end_time == "12:00"
    assert visit.enclosures == [enclosure1, enclosure2]


def test_visit_with_too_many_enclosures():
    enclosures = [Enclosure(i, f"Enclosure {i}", "large", ["species"]) for i in range(6)]
    with pytest.raises(ValueError):
        Visit(1, "2024-06-19", "10:00", "12:00", enclosures)


# Tests pour la classe ZooManager
def test_zoo_manager_add_animal():
    zoo_manager = ZooManager()
    animal = Animal(1, "Simba", "lion", 5, None)
    zoo_manager.add_animal(animal)
    assert zoo_manager.animals[1] == animal


def test_zoo_manager_modify_animal():
    zoo_manager = ZooManager()
    animal = Animal(1, "Simba", "lion", 5, None)
    zoo_manager.add_animal(animal)
    zoo_manager.modify_animal(1, name="Nala", age=6)
    modified_animal = zoo_manager.animals[1]
    assert modified_animal.name == "Nala"
    assert modified_animal.age == 6


def test_zoo_manager_remove_animal():
    zoo_manager = ZooManager()
    animal = Animal(1, "Simba", "lion", 5, None)
    zoo_manager.add_animal(animal)
    zoo_manager.remove_animal(1)
    assert 1 not in zoo_manager.animals


def test_zoo_manager_add_enclosure():
    zoo_manager = ZooManager()
    enclosure = Enclosure(1, "Big Cats", "large", ["lion", "tiger"])
    zoo_manager.add_enclosure(enclosure)
    assert zoo_manager.enclosures[1] == enclosure


def test_zoo_manager_modify_enclosure():
    zoo_manager = ZooManager()
    enclosure = Enclosure(1, "Big Cats", "large", ["lion", "tiger"])
    zoo_manager.add_enclosure(enclosure)
    zoo_manager.modify_enclosure(1, name="Small Cats", size="medium")
    modified_enclosure = zoo_manager.enclosures[1]
    assert modified_enclosure.name == "Small Cats"
    assert modified_enclosure.size == "medium"


def test_zoo_manager_remove_empty_enclosure():
    zoo_manager = ZooManager()
    enclosure = Enclosure(1, "Big Cats", "large", ["lion", "tiger"])
    zoo_manager.add_enclosure(enclosure)
    zoo_manager.remove_enclosure(1)
    assert 1 not in zoo_manager.enclosures


def test_zoo_manager_remove_non_empty_enclosure():
    zoo_manager = ZooManager()
    enclosure = Enclosure(1, "Big Cats", "large", ["lion", "tiger"])
    animal = Animal(1, "Simba", "lion", 5, None)
    enclosure.add_animal(animal)
    zoo_manager.add_enclosure(enclosure)
    with pytest.raises(ValueError):
        zoo_manager.remove_enclosure(1)


def test_zoo_manager_add_visit():
    zoo_manager = ZooManager()
    enclosure1 = Enclosure(1, "Big Cats", "large", ["lion", "tiger"])
    enclosure2 = Enclosure(2, "Reptile House", "medium", ["snake", "lizard"])
    visit = Visit(1, "2024-06-19", "10:00", "12:00", [enclosure1, enclosure2])
    zoo_manager.add_visit(visit)
    assert zoo_manager.visits[1] == visit


def test_zoo_manager_modify_visit():
    zoo_manager = ZooManager()
    enclosure1 = Enclosure(1, "Big Cats", "large", ["lion", "tiger"])
    enclosure2 = Enclosure(2, "Reptile House", "medium", ["snake", "lizard"])
    visit = Visit(1, "2024-06-19", "10:00", "12:00", [enclosure1, enclosure2])
    zoo_manager.add_visit(visit)
    zoo_manager.modify_visit(1, start_time="11:00", end_time="13:00")
    modified_visit = zoo_manager.visits[1]
    assert modified_visit.start_time == "11:00"
    assert modified_visit.end_time == "13:00"


def test_zoo_manager_remove_visit():
    zoo_manager = ZooManager()
    enclosure1 = Enclosure(1, "Big Cats", "large", ["lion", "tiger"])
    enclosure2 = Enclosure(2, "Reptile House", "medium", ["snake", "lizard"])
    visit = Visit(1, "2024-06-19", "10:00", "12:00", [enclosure1, enclosure2])
    zoo_manager.add_visit(visit)
    zoo_manager.remove_visit(1)
    assert 1 not in zoo_manager.visits
