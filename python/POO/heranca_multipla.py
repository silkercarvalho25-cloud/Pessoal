"""
class Cachorro:
    def __init__(self,nome):
        self.nome = nome

    def movimento (self):
        print("O animal se movimenta")

cachorro1 = Cachorro("Rex")
print(cachorro1.nome)
cachorro1.movimento()
"""

class Animal:
    def __init__(self,patas):
        self.patas = patas

    def andar (self):
        print("O animal anda")

class Cachorro (Animal):
    def __init__(self, patas,nome):
        self.nome = nome
        super().__init__(patas)

pitbull = Cachorro(5,"Rex")
print(pitbull.patas)
pitbull.andar()