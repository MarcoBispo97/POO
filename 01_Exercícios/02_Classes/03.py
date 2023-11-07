# 3. Desenvolva um programa que represente um animal. O programa deve ter uma classe Animal que tenha os atributos nome, espécie, idade e habitat. O programa deve também ter um método imprimir_dados() que imprima os dados do animal.

# Enredo:

# Imagine que você está desenvolvendo um programa para um zoológico. Você precisa criar um programa que possa representar um animal. O programa deve ter os seguintes atributos:

# Nome: o nome do animal
# Espécie: a espécie do animal
# Idade: a idade do animal
# Habitat: o habitat do animal
# O programa também deve ter um método imprimir_dados() que imprima os dados do animal.

class Animal():

    def __init__(self, nome: str, especie: str, idade: int, habitat: str):
        self.nome = nome
        self.especie = especie
        self.idade = idade
        self.habitat = habitat

    def imprimir_dados(self):
        print(f"nome {self.nome}")
        print(f"especie {self.especie}")
        print(f"idade {self.idade}")
        print(f"habitat {self.habitat}")


Ganso = Animal('ganso', 'branco', 4, 'mata')
Ganso.imprimir_dados()
Elefante = Animal('Elefante', 'Africano', 80, 'Africa')
Elefante.imprimir_dados()
