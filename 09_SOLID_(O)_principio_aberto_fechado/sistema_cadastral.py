# O open close and principal
# entradas diferentes deram acoes diferentes
class Circo:

    def apresentar(self, apresentador: any):
        apresentador.apresentar_show()

    # def apresentar_malabarista(self):
    #     print('Malabarista apresentando seu show')

    # def apresentar_palhaco(self):
    #     print('Palhaco apresentando seu show')


class Malabarista:

    def apresentar_show(self):
        print('Malabarista apresentando seu show')


class Palhaco:

    def apresentar_show(self):
        print('Palhaco apresentadno seu show')


circo = Circo()
malabarista = Malabarista()
palhaco = Palhaco()

circo.apresentar(malabarista)
circo.apresentar(palhaco)

# Conceiro de módulo aberto
