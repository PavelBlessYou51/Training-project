from dataclasses import dataclass


@dataclass
class Person:
    full_name: str = None
    email: str = None
    current_addres: str = None
    permanent_addres: str = None
