from dataclasses import dataclass


@dataclass
class Seller:
    id = None
    name = None

    def __init__(self, id, name):
        self.id = id
        self.name = name
