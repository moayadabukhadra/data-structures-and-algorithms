
from data_structures_and_algorithms.stack_queue_animal_shelter.stack_queue_animal_shelter import AnimalShelter , Cat , Dog
import pytest
import unittest


def test_enqueue():
    shelter = AnimalShelter()
    cat1=Cat()
    shelter.enqueue(cat1)
    actual=shelter.front
    expected=cat1
    assert actual==expected

def test_enqueue_multible_animals():
    "tests the enqueue using the size function and the animal at the front in the shelter"
    shelter=AnimalShelter()
    cat1=Cat()
    dog1=Dog()
    cat2=Cat()
    dog2=Dog()
    animal_list=[cat1,dog1,cat2,dog2]
    for aniaml in animal_list:
        shelter.enqueue(aniaml)
    actual = shelter.size()
    expected=4
    assert actual == expected
    actual= shelter.front.type
    expected="cat"
    assert actual==expected

def test_enqueue_multible_animals_using_str():
    shelter=AnimalShelter()
    cat1=Cat()
    dog1=Dog()
    cat2=Cat()
    dog2=Dog()
    animal_list=[cat1,dog1,cat2,dog2]
    for aniaml in animal_list:
        shelter.enqueue(aniaml)

    actual=shelter.__str__()
    expected="first animal --> cat --> dog --> cat --> dog --> None"
    assert actual==expected

def test_dequeue(animals):
    actual =animals.dequeue("cat")
    expected="cat"
    assert actual==expected

def test_empty_shlter_using_dequeue(animals):
    size=animals.size()
    for i in range(0,size):
        animals.dequeue("any")
    actual=animals.is_empty()
    expected=True
    assert actual==expected

class TestQueue(unittest.TestCase):
    def test_dequeue_empty_shelter(self):
        shelter=AnimalShelter()
        with self.assertRaises(Exception):
            shelter.dequeue()
    def test_enqueue_not_dogs_cats(self):
        shelter=AnimalShelter()
        with self.assertRaises(ValueError):
            shelter.enqueue("any")



@pytest.fixture
def animals():
    animals=AnimalShelter()
    animals
    cat1=Cat()
    dog1=Dog()
    cat2=Cat()
    dog2=Dog()
    cat3=Cat()
    dog3=Dog()
    cat4=Cat()
    dog4=Dog()
    animal_list=[cat1,dog1,cat2,dog2,cat3,dog3,cat4,dog4]
    for aniaml in animal_list:
        animals.enqueue(aniaml)
    return animals