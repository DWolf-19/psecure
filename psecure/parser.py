import math
import enum

import scipy


class Constants(enum.Enum):
    MATH_CONSTANTS = {
        "PI": math.pi,
        "E": math.e,
        # Golden ratio
        "GOLDEN": scipy.constants.golden
    }

class Parser:
    def __init__(self, expression: str):
        self.expression = expression.replace(" ", "")

    def parse(self, *args) -> int | float:
        pass
