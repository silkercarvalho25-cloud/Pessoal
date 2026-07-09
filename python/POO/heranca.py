class Veiculo:
    def __init__(self, cor, tamanho, placa, contagem_rodas):
        self.cor = cor
        self.tamanho = tamanho
        self.placa = placa
        self.contagem_rodas = contagem_rodas

    def barulho(self):
        print("BUZINANDOOOO")


class Motocicleta(Veiculo):  # clases filha de Veiculos
    pass


class Carro(Veiculo):
    pass


class Caminhao(Veiculo):
    def __init__(self, cor, tamanho, placa, contagem_rodas,carregado):
        super().__init__(cor, tamanho, placa, contagem_rodas)
        self.carregado = carregado

    def esta_carregado(self):
        print(
            f"{"sim," if self.carregado else "nao,"} estou carregado")


moto = Motocicleta("vermelha", "Porte Pequeno", "MOTO-6521", "2 roads")
print(moto)
print(moto.cor)
print(moto.tamanho)
moto.barulho()


carro = Carro("branco", "Porte Grande", "CARRO-6525", "4 rodas")
print(carro.tamanho)
print(carro.cor)
print(carro.placa)
carro.barulho()


caminhao = Caminhao("Pretao", "Porte grande", "CAMINHAO-5641", "6 rodas",False)
print(caminhao.cor)
print(caminhao.tamanho)
print(caminhao.placa)
caminhao.barulho()
caminhao.esta_carregado()