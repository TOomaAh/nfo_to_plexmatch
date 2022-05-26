import string


class File:

    def __init__(self, name: str, path: str):
        self.name = name
        self.path = path

    def __str__(self):
        return f"File ( name: {self.name}, path: {self.path} )"

    def __repr__(self):
        return f"File('{self.name}, {self.path}')"