"""The module for creating testing data"""
import os
import random

from faker import Faker

from data.data import Person

faker_en = Faker('En')
faker_en_us = Faker('en_US')


def create_person():
    return Person(
        full_name=faker_en.name(),
        email=faker_en.email(),
        current_addres=faker_en.address(),
        permanent_addres=faker_en.address(),
        age=str(random.randint(20, 50)),
        salary=str(random.randint(10000, 100000)),
        department=faker_en.street_name(),
        phone_number=faker_en_us.msisdn()
    )


def string_handler(title: str) -> str:
    result = title.lower()
    if '.' in title:
        return result.split()[0] + 'File'
    return result


def file_generator() -> str:
    path = os.getcwd() + r'\filetest.txt'
    file = open(path, '+w', encoding='utf-8')
    file.write('Hello World!')
    file.close()
    return path
