# 2. Desenvolva um programa que represente uma pessoa. O programa deve ter uma classe Pessoa que tenha os atributos nome, idade, sexo e endereço. O programa deve também ter um método imprimir_dados() que imprima os dados da pessoa.

# Enredo:

# Imagine que você está desenvolvendo um programa para uma empresa. Você precisa criar um programa que possa representar uma pessoa. O programa deve ter os seguintes atributos:

# Nome: o nome da pessoa
# Idade: a idade da pessoa
# Sexo: o sexo da pessoa
# Endereço: o endereço da pessoa
# O programa também deve ter um método imprimir_dados() que imprima os dados da pessoa.

class Pessoa():
    def __init__(self, nome: str, idade: int, sexo: str, endereco: str):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.endereco = endereco

    def imprimir_dados(self):
        print(f'nome: {self.nome}')
        print(f'idade: {self.idade}')
        print(f'sexo: {self.sexo}')
        print(f'endereço: {self.endereco}')


P1 = Pessoa('Marco', 26, 'Masculino', 'Taubaté')
P1.imprimir_dados()
P2 = Pessoa('Gabriela', 27, 'Feminino', 'Ubatuba')
P2.imprimir_dados()
