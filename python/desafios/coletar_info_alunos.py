"""
Nome: Lucas
Idade: 20
Nota: 8.5
"""

nome_do_aluno = input("Qual nome do aluno?:")
idade_do_aluno = input("Qual a idade do aluno?:")
nota_do_aluno = input("Qual a nota do aluno?:")

dados_aluno = {
            "dados":{"nome":{nome_do_aluno},
                    "idade":{idade_do_aluno},
                    "nota":{nota_do_aluno}}
    }

while True:
    print("\nOque vc quer saber do aluno?")
    print("""
    Nome - 1
    Idade - 2
    Nota - 3
    Sair - 4
    """)
    resposta = input("Ensira o numero:")

    if resposta == "1":
        print(dados_aluno["dados"]["nome"])

    elif resposta == "2":
        print(dados_aluno["dados"]["idade"])

    elif resposta == "3":
        print(dados_aluno["dados"]["nota"])
    
    elif resposta == "4":
        break
    else:
        print("Ensira os dados certos")