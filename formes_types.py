import math
from typing import ClassVar, List, Tuple
from dataclasses import dataclass
from abc import ABC, abstractmethod


@dataclass
class Forme(ABC):
    formes: ClassVar[List['Forme']] = []
    position: Tuple[float, float]

    @classmethod
    def nb_formes(cls) -> int:
        return len(cls.formes)

    def __post_init__(self):
        Forme.formes.append(self)

    @abstractmethod
    def perimetre(self) -> float:
        ...


@dataclass
class Cercle(Forme):
    rayon: float

    def perimetre(self) -> float:
        return 2 * math.pi * self.rayon


@dataclass
class Rectangle(Forme):
    largeur: float
    hauteur: float

    def perimetre(self) -> float:
        return self.largeur * self.hauteur


c1 = Cercle((0, 0), 20)
c2 = Cercle((10, 10), 10)
r1 = Rectangle((5, 5), 20, 10)
r2 = Rectangle((10, 5), 5, 10)
print(f"{Forme.nb_formes()} formes, leur périmètre :")
for forme in Forme.formes:
    perimetre = forme.perimetre()
    print(f"- {forme} : {perimetre}")
