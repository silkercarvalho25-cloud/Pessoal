exemplo1 = "Et dolor fugiat eu ex ex"
exemplo2 = "      Incididunt id eu consectetur nisi               "
exemplo3 = "Nostrud"

print(exemplo1.upper()) # todas as palavras em maiusculo
print(exemplo1.lower()) # todas as palavras em minusculo
print(exemplo1.title()) # primeira palavra em maiusculos

print()

print(exemplo2)
print(exemplo2.strip() + ".") #tira os espaços de ambos os lados
print(exemplo2.lstrip() + ".") #tira os espaços da esquerda
print(exemplo2.rstrip() + ".") #tira os espaços da direita

print()

print(exemplo3.center(15,"#")) #preenche os espaçoes em branco para dar a quantidade de caracteres que vc quer
print("-".join(exemplo3)) #coloca um caractere em cada espaço entre as letras