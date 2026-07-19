class Times_de_Futebol:
    def __init__(self,conhecimento,cor,principais,patrocinio):
        self.conhecimento = conhecimento
        self.cor = cor
        self.principais = principais
        self.patrocinio = patrocinio
    def grito (self):
        print("VAAAAIIIII!!!!!!!")

class Corinthinas (Times_de_Futebol):
    pass

class Palmeiras (Times_de_Futebol):
    pass

class Fluminense (Times_de_Futebol):
    def __init__(self, conhecimento, cor, principais, patrocinio,situacao_porcentagem):
        super().__init__(conhecimento, cor, principais, patrocinio)
        self.situacao_porcentagem = situacao_porcentagem
    
    def dificuldade (self):
        print(f"{"muito boa" if self.situacao_porcentagem > 90  else "muito ruim"}")

corinthinas = Corinthinas("famososo","preto e branco","Memphins","Nike")
print(corinthinas.cor)
print(corinthinas.principais)
print(corinthinas.patrocinio)

palmeiras = Palmeiras("é, tentam","Verdekkkk","uma la e um aqui","KKKKKKKKK falidos")
print(palmeiras.patrocinio)
print(palmeiras.cor)
print(palmeiras.principais)
print(palmeiras.conhecimento)

fluminense = Fluminense("de boas até","verde e vermelha","marcio e antonio","adidas",95)
print(fluminense.conhecimento)
print(fluminense.cor)
print(fluminense.principais)
print(fluminense.patrocinio)
fluminense.grito()
fluminense.dificuldade()