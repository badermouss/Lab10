from dataclasses import dataclass

from model.countries import Country


@dataclass
class Contiguity:
    state1: Country
    state2: Country

    def __str__(self):
        return f"Arco: {self.state1} - {self.state2}"
