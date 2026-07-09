class Cachorro:
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca

    def latir(self):
        print(f"{self.nome} está latindo: Au au!")


dog_1 = Cachorro("Rex", "Shitsu")

dog_2 = Cachorro("Dexter", "Shitsu")

dog_1.latir()

dog_2.latir()