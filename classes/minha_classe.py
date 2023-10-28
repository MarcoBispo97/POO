# Classe é uma abstacao de um elemnto natura que possui ACOES_(METODOS) E CARACTERISTICAS_(ATRIBUTOS)

class MinhaClasse:
    # metodo construtor
    # metodo que define a nossa classe
    def __init__(self, att):
        self.meu_atributo = 'Ola Mundo'
        self.meu_atributo2 = att

    def meu_metodo(self):  # o que vai entrar na minha classe, minha referencia
        print(self.meu_atributo)
        print(self.meu_atributo2)

    def meu_metodo2(self, num, mult):
        return num * mult


# Instanciando o obj da minha classe
objeto = MinhaClasse(23)
objeto.meu_metodo()
