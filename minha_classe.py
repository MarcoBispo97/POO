# Classe é uma abstacao de um elemnto natura que possui ACOES_(METODOS) E CARACTERISTICAS_(ATRIBUTOS)

class MinhaClasse:
    # metodo construtor
    def __init__(self):
        self.meu_atributo = 'Ola Mundo'

    def meu_metodo(self):  # o que vai entrar na minha classe, minha referencia
        print('Estou no metodo!')

    def meu_metodo2(self, num, mult):
        return num * mult


# Instanciando o obj da minha classe
objeto = MinhaClasse()
result = objeto.meu_metodo2(3, 2)
print(result)
