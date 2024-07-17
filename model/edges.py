from dataclasses import dataclass
@dataclass
class Archi:
    cromosoma1: int
    cromosoma2: int
    expression_corr: float

    def __str__(self):
        print(f"{self.cromosoma1}{self.cromosoma2}{self.expression_corr}")

