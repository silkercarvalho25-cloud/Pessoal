"""
Faça o programa informar:

Aprovado (nota ≥ 7)
Recuperação (nota entre 5 e 6.9)
Reprovado (nota < 5)
"""

nome_aluno = input("Qual nome do aluno?:")
nota_aluno = float(input("Qual a nota do aluno?:"))

dados_aluno = {
    "dados":{"nome":{nome_aluno},
               "nota":{nota_aluno}}
}

while True:
    print("oque vc quer saber do aluno?")
    print("""
1 - Nome
2 - Nota
3 - Situação
4 - Sair    
""")
    resposta = input("Escolha o Numero:")
    if resposta == "1":
        print(dados_aluno["dados"]["nome"])
    elif resposta == "2":
        print(dados_aluno["dados"]["nota"])
    elif resposta == "3":
        if nota_aluno >= 7:
            print("Ele foi aprovado")
        elif nota_aluno > 5 and nota_aluno <= 6.9:
            print("Ele ta de recuperação")
        else:
            print("Ele foi reprovado")
    else:
        print("Encerrando...")
        break