comeco = int(input("comeco por onde?"))
numero = int(input("vou até q numero?: "))
pular = int(input("pulando de quanto em quanto?: "))

for numero in range(numero+1): #range usado para repetiçoes, o +1 para ir até o numero digitado
    print(numero, end=" - ")

print()

for numero in range(comeco, numero+1, pular): #aqui ja vemos completo,(inicio, até o numero q vc escolheu, de qual maneira)
    print(numero, end=" - ")
