"""The module for creating testing data"""
import os
import random

from faker import Faker

from data.data import Person, Date

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

def get_colors(count: int) -> list[str]:
    tuple_of_colors = ("Red", "Blue", "Green", "Yellow", "Purple", "Black", "White", "Voilet", "Indigo", "Magenta", "Aqua")
    list_for_return = list()
    while len(list_for_return) != count:
        color = random.choice(tuple_of_colors)
        if color in list_for_return:
            continue
        list_for_return.append(color)
    return list_for_return

def date_generator() -> Date:
    return Date(
        day=faker_en.day_of_month(),
        month=faker_en.month_name(),
        year=faker_en.year(),
        time='12:00'
    )