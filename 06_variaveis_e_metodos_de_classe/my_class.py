class MinhaClasse:
    # Metodo construtor
    # Para oq serve o self

    estatico = 'lhama'  # Variavel de classe ou variaveis estaticas

    def __init__(self, estado) -> None:
        self.estado = estado


obj1 = MinhaClasse(True)
obj2 = MinhaClasse(False)
obj1.estatico = 'Programador'

print(obj1.estatico)
print(obj2.estatico)
print(MinhaClasse.estatico)

MinhaClasse.estatico = 'MinhaClasse'

print(obj1.estatico)
print(obj2.estatico)
print(MinhaClasse.estatico)
