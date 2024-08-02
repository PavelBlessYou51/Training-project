"""The module for creating testing data"""
from faker import Faker

from data.data import Person

faker_en = Faker('En')


def create_person():
    return Person(
        full_name=faker_en.name(),
        email=faker_en.email(),
        current_addres=faker_en.address(),
        permanent_addres=faker_en.address()
    )

