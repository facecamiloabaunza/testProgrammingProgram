from dataclasses import dataclass


@dataclass
class Parameter:
    id = None
    code = None
    value = None

    def __init__(self, id, code, value):
        self.id = id
        self.code = code
        self.value = value
