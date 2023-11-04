class Interruptor:
    def __init__(self, comodo: str):
        self.__comodo = comodo

    def ascender(self):
        print('acesndendo {}'.format(self.__comodo))

    def apagar(self):
        print('apagando {}'.format(self.__comodo))

class Pessoa:
    def acender_luz(self, Interruptor: Type[Interruptor]):
        Interruptor.acender()
    
    def apagar_luz(self, interruptor: Type[Interruptor]):
        interruptor.apagar

    def dormir(self):
        print('Fui dormir')

lhama = Pessoa()
interruptor_quarto = Interruptor('quarto')

interruptor_quarto.ascender

