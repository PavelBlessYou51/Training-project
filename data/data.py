from dataclasses import dataclass


@dataclass
class Person:
    full_name: str = None
    email: str = None
    current_addres: str = None
    permanent_addres: str = None
    age: str = None
    salary: str = None
    department: str = None
    phone_number: str = None

@dataclass
class Date:
    day: str = None
    month: str = None
    year: str = None
    time: str = None
