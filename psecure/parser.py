import math


class Parser:
    __slots__ = ("expression", "position")

    FUNCTIONS = {
        "abs": abs,
        "sqrt": math.sqrt
    }

    CONSTANTS = {
        "PI": math.pi,
        "E": math.e
    }

    def __init__(self, expression: str):
        self.expression = expression.replace(" ", "")

        self.position = 0

    def parse(self, *args) -> int | float:
        self.position = 0  # Reset

        while self.position < len(self.expression):
            pass

    def split_number(self):
        pass
