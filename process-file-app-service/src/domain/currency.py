from dataclasses import dataclass


@dataclass
class Currency:
    id = None
    description = None
    

    def __init__(self, id, description):
        self.id = id
        self.description = description
