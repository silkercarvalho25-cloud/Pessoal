class Animal:
    def __init__(self, nome, idade, peso):
        self.nome = nome
        self.idade = idade
        self.peso = peso

    def emitir_som(self):
        print("Som do Animal")


class Cachorro(Animal):
    def emitir_som(self):
        print("AU AU !") # o som do animal é reescrito por essa parte, por conta q quando chama essa atributo
                        #ele ja procura nao mais proximo, e nao no mais longe, ja achou a resposta no objeto Cachorro,
                        #nao precisa ir no Animal
class Gato(Animal):
    def emitir_som(self):
        print("Miau!")

class Passaro(Animal):
    def emitir_som(self):
        print("Piu Piu!")


cachorro = Cachorro("Rex",10,55)
cachorro.emitir_som()# quando o emitir som é chamado, ele vai direto no objeto q ele ta associado, e nao no principal PAI

gato = Gato("Felix",15,33)
gato.emitir_som()

passaro = Passaro("Bethoven",8,20)
passaro.emitir_som()