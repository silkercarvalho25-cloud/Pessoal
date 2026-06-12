nome = input("Digite o seu nome:")
idade = input("Digite sua idade:")

print(f"ola {nome} da idade {idade}")
print(f"ola {nome} da idade {idade}", end= "... \n") #adiciona algo no final da sentença e o [\n] para quebra de linha
print(nome, idade, sep= "#") #caso estejam soltas as informaçoes, cada espaço adicioan algo dentro q esta nos " "
print(nome,idade, sep = "#", end= "...")