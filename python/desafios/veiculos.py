class Veiculos:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def ligar(self):
        print("O veiculos ligou")


class Carro(Veiculos):
    def ligar(self):
        print("O carro ligou.")


class Moto(Veiculos):
    def ligar(self):
        print("A moto ligou.")


class Caminhao(Veiculos):
    def ligar(self):
        print("O caminhão ligou.")
