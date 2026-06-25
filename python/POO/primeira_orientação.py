class Bicicleta:  # Criar class e definir o nome da classe
    def __init__(self, cor, ano, marca, preco):  # Criar metodo construtor
        self.cor = cor
        self.ano = ano
        self.marca = marca
        self.preco = preco

    def buzinar(self):  # definindo um método
        print("PAAAAAAAAAAAAAAA")

    def grau(self):
        print("Dando grau de bicicleta")

    def parar(self):
        print("Freiando a bicicleta")

    def __str__(self):
        return f"{self.__class__.__name__}:{", ".join([f"{chave} = {valor}" for chave, valor in self.__dict__.items()])}"


bicicleta = Bicicleta("Verde", 2005, "Caloi", 20000)

bicicleta.buzinar()
bicicleta.grau()
bicicleta.parar()

print(  # acesse pelo atributos os valores e infoaçoes da bicicleta
    bicicleta.cor, bicicleta.ano
)

print(bicicleta.cor)

print(bicicleta)