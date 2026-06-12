nome = "silker"
idade = 20
dados = {"nome": "silker", "idade": 20}
dinheiro = 10.65265

print("seu nome é: %s Idade: %d" % (nome, idade))

print("Seu nome é: {} Idade: {}".format(nome, idade))

print("Seu nome é: {1} Idade: {0}".format(idade, nome))

print()

print("Seu nome é: {nome} Idade: {idade}".format(idade=idade, nome=nome))

print("Seu nome é: {nome} Idade: {idade}".format(**dados))

print(f"Seu nome é: {nome} Idade: {idade} voce tem {dinheiro :.1f} reais")