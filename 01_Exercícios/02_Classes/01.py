# 1. Desenvolva um programa que represente um carro. O programa deve ter uma classe Carro que tenha os atributos cor, modelo, ano e placa. O programa deve também ter um método imprimir_dados() que imprima os dados do carro.

# Enredo:

# Imagine que você está desenvolvendo um programa para uma concessionária de carros. Você precisa criar um programa que possa representar um carro. O programa deve ter os seguintes atributos:

# Cor: a cor do carro
# Modelo: o modelo do carro
# Ano: o ano de fabricação do carro
# Placa: a placa do carro
# O programa também deve ter um método imprimir_dados() que imprima os dados do carro.

class Carro:
    def __init__(self, cor: str, modelo: str, ano: int, placa: str):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.placa = placa

    def imprimir_carro(self):
        print(f"Cor: {self.cor}")
        print(f"Modelo: {self.cor}")
        print(f"Ano: {self.cor}")
        print(f"Placa: {self.cor}")


celta = Carro('azul', 'celta', 2002, 'AB123')
celta.imprimir_carro()
chevete = Carro('preto', 'chevete', 1985, 'ABc1423')
chevete.imprimir_carro()
