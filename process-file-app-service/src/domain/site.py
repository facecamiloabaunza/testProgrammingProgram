from dataclasses import dataclass


@dataclass
class Site:
    id = None
    categories = []

    def __init__(self, id,categories):
        self.id = id
        self.categories = categories
