def exibir_mensagem(): # def definindo que "exibir_mensagem()" sera´um  funçao
    print("Ola Mundo!") # parametro dado a oque esta funçao ira fazer ou retornar

exibir_mensagem()  # ativa a função

print("=" * 50)

# =========================
# Linha 1
# =========================


def exibir_mensagem_2(nome):
    print(f"Ola, soube que seu nome é {nome}")

exibir_mensagem_2("silker")

print("=" * 50)

# =========================
# Linha 2
# =========================


def calcular_total(numeros):
    return sum(numeros) #sum para somar todos os valores


def retorna_maior_e_menor(numero):
    antes = numero - 1
    depois = numero + 1

    return antes, depois


print(calcular_total([9, 210, 21, 65, 20]))
print(retorna_maior_e_menor(20))

print("=" * 50)

# =========================
# Linha 3
# =========================


def carro_parte(marca, modelo, ano, placa):
    print(f"Carro planejado com Sucesso | {marca} | {modelo} | {ano} | {placa}")


carro_parte("Fiat", "Palio", 1997, "abc-2101")
carro_parte(
    **{
        "marca": "Fiat",
        "modelo": "Palio",
        "ano": 1997,
        "placa": "abc-2101"
    }
)  # ** para criar um dicionarios

print("=" * 50)

# =========================
# Linha 4
# =========================

# [nada] = identifica por posiçao
# / = identifica por posiçao e nome
# * = identifica por nome


def criando_carro(motor, marca, cor, /, dono, ano):
    print(f"Seu carro é {motor} | {marca} | {cor} | {dono} | {ano}")


criando_carro("1,0", "Fiat", "azul", dono="silker", ano=1995)


def criar_carro(*, modelo, ano, cor):
    print(f"Seu carro é {modelo} | {ano} | {cor}")


criar_carro(modelo="Fiat", ano="1957", cor="amarelo")

print("=" * 50)

# =========================
# Linha 5
# =========================


def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def exibir_os_resultados(a, b, funcao):
    resultado = funcao(a, b)
    print(f"Resultado igual ao  = {resultado}")


exibir_os_resultados(10, 15, somar)
exibir_os_resultados(12, 85, subtrair)
print(somar(12, 74))

print("=" * 50)

# =========================
# Linha 6
# =========================

salario = 2000


def calculo_do_salaro(bonus):
    global salario  # global pq a variavel salario esta fora do escopo
    salario += bonus
    return salario


resultado = calculo_do_salaro(500)
print(resultado)