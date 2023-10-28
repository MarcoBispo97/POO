# encpsulamento, polimorfismo e herenca sao os pilares de POO
# Encapsulamento - Permissoes de uso e contexto

class Pessoa:

    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.__cpf = cpf

    def print_cpf(self):
        print(self.__cpf)

    def correr(self):
        print('Estou correndo')

    def beber(self, bebida):
        if bebida == 'cerveja':
            self.__apresentar_documento()
        print('bebendo...')

    # duplo __ ele nao deixa acessivel
    def __apresentar_documento(self):
        print(self.__cpf)


ronaldo = Pessoa('Ronaldo', 32, '657tas78da')
ronaldo.beber('cerveja')
ronaldo.beber('coca-cola')
