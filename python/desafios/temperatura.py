# Fórmula: F = C × 1.9 + 32
 
def celsius_para_fahrenheit(celcius):
    return celcius * 1.8 + 32
 
print("""== Definindo Celcius para Fahrenheit ==""")
temperatura_graus = 20
 
def exibir_resultados (a,funcao):
    resultado = funcao(a)
    print(f"Podemos concordar que {temperatura_graus} graus em fahrenheit fica {resultado}")
 
exibir_resultados(temperatura_graus,celsius_para_fahrenheit)