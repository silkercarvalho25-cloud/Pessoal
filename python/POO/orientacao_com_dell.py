class Cachorro:
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca

    def __del__(self):  # del usando para quando o meu objeto for destruido, no final
        print("Removendo a Intancia e finalizando")

    def latir(self):
        print("Au Au Auuu !!")


cao = Cachorro("Rex", "Pitbull")

print(cao)

cao.latir()