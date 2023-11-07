# Em programação orientada a objetos (POO), o encapsulamento é um dos quatro princípios fundamentais, juntamente com herança, polimorfismo e abstração. O encapsulamento é o conceito de esconder os detalhes internos de um objeto e fornecer uma interface pública para interagir com ele. Em Python, como em muitas outras linguagens de programação orientada a objetos, o encapsulamento é implementado usando classes e modificadores de acesso.

# Existem três níveis de controle de acesso que podem ser usados em Python para definir o encapsulamento:

# Público: Os membros de uma classe são públicos por padrão e podem ser acessados de qualquer lugar fora da classe. Eles são acessados usando a notação de ponto.
# Exemplo:

class MinhaClasse:
    def __init__(self):
        self.var_publica = 10


obj = MinhaClasse()
print(obj.var_publica)  # Acesso público


# Protegido: Os membros protegidos de uma classe têm um sublinhado (_) como prefixo no nome. Embora eles possam ser acessados fora da classe, é uma convenção indicar que eles não devem ser acessados diretamente.

class MinhaClasse:
    def __init__(self):
        self._var_protegida = 20


obj = MinhaClasse()
print(obj._var_protegida)  # Acesso protegido (não recomendado)


# Privado: Os membros privados de uma classe têm dois sublinhados (__) como prefixo no nome. Eles são mais restritos e não podem ser acessados diretamente fora da classe. No entanto, eles ainda podem ser acessados usando um nome especial que o Python gera.

class MinhaClasse:
    def __init__(self):
        self.__var_privada = 30


obj = MinhaClasse()
# Tentar acessar __var_privada diretamente gera um erro
# print(obj.__var_privada)

# Acessar __var_privada usando o nome gerado pelo Python
print(obj._MinhaClasse__var_privada)  # Acesso privado (não recomendado)
