contador = 0
frase = "Programação"
for conta_vogais in frase:
    if conta_vogais in "aeiouAEIOU":
        contador = contador + 1
print(f"O número de vogais na string '{frase}' é: {contador}")