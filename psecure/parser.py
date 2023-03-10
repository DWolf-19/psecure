import math
import enum

import scipy.constants


class Constants(enum.Enum):
    MATH_CONSTANTS = {
        "pi": math.pi,
        "e": math.e,
        # Golden ratio
        "golden": scipy.constants.golden
    }

    PHYSIC_CONSTANTS = {
        # Speed of light in vacuum
        "c": scipy.constants.c,
        # The magnetic constant
        "mu_0": scipy.constants.mu_0,
        # The electric constant (vacuum permittivity)
        "epsilon_0": scipy.constants.epsilon_0,
        # The Planck constant
        "h": scipy.constants.h,
        # h / (2 * pi)
        "hbar": scipy.constants.hbar,
        # Newtonian constant of gravitation
        "G": scipy.constants.G,
        # Standard acceleration of gravity
        "g": scipy.constants.g,
        # Elementary charge
        "ec": scipy.constants.e,
        # Molar gas constant
        "R": scipy.constants.R,
        # Fine-structure constant
        "alpha": scipy.constants.alpha,
        # Avogadro constant
        "N_A": scipy.constants.N_A,
        # Boltzmann constant
        "k": scipy.constants.k,
        # Stefan-Boltzmann constant
        "sigma": scipy.constants.sigma,
        # Wien displacement law constant
        "Wien": scipy.constants.Wien,
        # Rydberg constant
        "Rydberg": scipy.constants.Rydberg,
        # Electron mass
        "m_e": scipy.constants.m_e,
        # Proton mass
        "m_p": scipy.constants.m_p,
        # Neutron mass
        "m_n": scipy.constants.m_n
    }

class Operations:
    @staticmethod
    def add(a: int | float, b: int | float) -> int | float:
        return a + b

    @staticmethod
    def sub(a: int | float, b: int | float) -> int | float:
        return a - b

    @staticmethod
    def mul(a: int | float, b: int | float) -> int | float:
        return a * b

    @staticmethod
    def div(a: int | float, b: int | float) -> int | float:
        return a / b

    @staticmethod
    def pow(a: int | float, b: int | float) -> int | float:
        return a ** b

    @staticmethod
    def mod(a: int | float, b: int | float) -> int | float:
        return a % b

class Parser:
    def __init__(self, expression: str):
        self.expression = expression.replace(" ", "")

    def parse(self, *args) -> int | float:
        pass
