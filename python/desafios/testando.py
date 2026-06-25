def calcular_numeros(a,b,c,d):

    somar = a + b
    subtrair = c - d
    
    return somar,subtrair

primeiro_numero = float(input("Escolha o primeiro numero da soma:"))
segundo_numero = float(input("Escolha o outro numero da soma:"))


terceiro_numero = float(input("Escolha o outro numero da subtrair:"))
quarto_numero = float(input("Escolha o outro numero da subtrair:"))

print(calcular_numeros(primeiro_numero,segundo_numero,terceiro_numero,quarto_numero))