class Pessoa:  # Substantivo

    def __init__(self, name: str, idade: int) -> None:
        self.name = name  # Substantivo
        self.idade = idade  # Substantivo

    def dirigir(self, veiculo: str) -> None:  # Verbos
        print('Dirigindo um(a) {}'.format(veiculo))

    def cantar(self) -> None:  # Verbos
        print('lalalala')

    def apresentar_idade(self) -> int:  # Verbos
        return self.idade
