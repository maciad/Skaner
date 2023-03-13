class Token:
    id: int
    value: str

    def __init__(self, id_, value_):
        self.id = id_
        self.value = value_

    def __str__(self):
        return f"id:{self.id}, val:'{self.value}'"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self.id == other.id and self.value == other.value



