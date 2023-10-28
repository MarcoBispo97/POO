# Com o encapsulamento o user  vai calcular apenas pela parte de cima, apenas por uma maneira
class Calculadora:
    def calcular(self, op, num1, num2):
        if op == '+':
            return self.__adicionar(num1, num2)
        elif op == '-':
            return self.__subtrair(num1, num2)
        else:
            print('Operacao invalida')

    def __adicionar(self, num1, num2):
        return num1 + num2

    def __subtrair(self, num1, num2):
        return num1 - num2


caculadora = Calculadora()
resultado = caculadora.calcular('+', 3, 2)
print(resultado)
