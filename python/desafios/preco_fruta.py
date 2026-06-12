"""
Exercício 3 - Estoque de Produtos

Crie um dicionário com três produtos.

Exemplo:

estoque = {
    "Maçã": 20,
    "Banana": 15,
    "Laranja": 8
}

Mostre:

Nome do produto
Quantidade

Utilize um for.
"""

primeira_fruta = input("Qual é a primeira fruta?:")
quantidade_da_primeira_fruta = int(input("Qual é a quantidade da primeira fruta?:"))

segunda_fruta = input("Qual é a segunda fruta?:")
quantidade_da_segunda_fruta = int(input("Qual é a quantidade da segunda fruta?:"))

terceira_fruta = input("Qual é a terceira fruta?:")
quantidade_da_terceira_fruta = int(input("Qual é a quantidade da terceira fruta?:"))

banco_de_dados_frutas = {
    "1 - fruta":{"nome":primeira_fruta,"quantidade":quantidade_da_primeira_fruta},
    "2 - fruta":{"nome":segunda_fruta, "quantidade":quantidade_da_segunda_fruta},
    "3 - fruta":{"nome":terceira_fruta, "quantidade":quantidade_da_terceira_fruta}
}

for frutas_for , dados_for in banco_de_dados_frutas.items():
    print(f"{frutas_for}: {dados_for["nome"]}, Quantidade: {dados_for["quantidade"]}")