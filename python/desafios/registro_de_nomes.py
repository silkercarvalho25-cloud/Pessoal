banco_de_dados = {
    "silker" :{"nome_completo":"Silker Carvalho", "idade":"19"},
    "samara" :{"nome_completo":"Samara Carva", "idade":"15"},
    "felipe" :{"nome_completo":"felipe silva", "idade":"07"}
}
while True:
    print("""
==== Bem - Vindo ao Banco do Cadastro ====
0 - Sair
1 - Ver cadastros existentes
2 - Cadastrar novo usuario
    """)
    resposta = input("Digite a sua Escolha:")
    if resposta == "0":
        print("Encerrando Programa...")
        break
    elif resposta == "2":
        nome_da_conta = str(input("Qual o nome da conta?:"))
        nome_completo_da_conta = str(input("Qual o nome completo da conta?:"))
        idade_da_conta = str(input("Qual a idade da conta?"))
        banco_de_dados.update({
            nome_da_conta:{
                "nome_completo": nome_completo_da_conta,
                "idade":idade_da_conta
                            }
        })
        print("Conta Atualizada com")
    elif resposta == "1":
        for chave, valor in banco_de_dados.items():
            nome = valor["nome_completo"]
            idade = valor["idade"]
            print(f"""
Nome: {chave}
Nome completo da Conta: {nome}
Idade do portador da Conta: {idade}""")