class Alarme():

    def __init__(self, estado: bool) -> None:
        self.estado = estado

    def get_estado(self) -> bool:
        return self.__estado

    def set_estado(self, valor: bool) -> None:
        self._estado = valor


al = Alarme(False)
