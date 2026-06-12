palavra = str(input("Escolha uma palavras:"))
escolhidas = "guilherme"


for quantidade in palavra: # o for vai dar a volta em cada letra por letra a string
    print(quantidade.upper(), end=" - ") #define o final, cancela a quebra de linha ou personalisa os espaços

print()#quebra de linha

for quantidade in palavra: # o for vai dar a volta em cada letra por letra a string
    # print(quantidade.upper(), end=" - ") #define o final, cancela a quebra de linha ou personalisa os espaços
    if quantidade in escolhidas:
        print(quantidade,end="")