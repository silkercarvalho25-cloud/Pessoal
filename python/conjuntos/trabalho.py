nome_primeira_pergunta = input("Qual o nome da primeira pessoa? ")
idade_primeira_pergunta = int(input("Qual a idade da primeira pessoa? "))

nome_segunda_pergunta = input("Qual o nome da segunda pessoa? ")
idade_segunda_pergunta = int(input("Qual a idade da segunda pessoa? "))

banco_de_dados = {
    "primeiros_dados": {
        "primeiro_nome": nome_primeira_pergunta,
        "primeira_idade": idade_primeira_pergunta
    },
    "segundos_dados": {
        "segundo_nome": nome_segunda_pergunta,
        "segunda_idade": idade_segunda_pergunta
    }
}
while True:
    print("\nO que você gostaria de saber?")
    print("""
1 - Nome do Primeiro Registrado
2 - Idade do Primeiro Registrado
3 - Nome do Segundo Registrado
4 - Idade do Segundo Registrado
5 - Ambos os Registros
6 - Sair
""")
    resposta = int(input("Escolha o número: "))
    if resposta == 1:
        print("Nome do Primeiro Registro:",
              banco_de_dados["primeiros_dados"]["primeiro_nome"])
    elif resposta == 2:
        print("Idade do Primeiro Registro:",
              banco_de_dados["primeiros_dados"]["primeira_idade"])
    elif resposta == 3:
        print("Nome do Segundo Registro:",
              banco_de_dados["segundos_dados"]["segundo_nome"])
    elif resposta == 4:
        print("Idade do Segundo Registro:",
              banco_de_dados["segundos_dados"]["segunda_idade"])
    elif resposta == 5:
        print("\nPrimeiro Registro:")
        print(
            f'Nome: {banco_de_dados["primeiros_dados"]["primeiro_nome"]}, '
            f'Idade: {banco_de_dados["primeiros_dados"]["primeira_idade"]}'
        )
        print("\nSegundo Registro:")
        print(
            f'Nome: {banco_de_dados["segundos_dados"]["segundo_nome"]}, '
            f'Idade: {banco_de_dados["segundos_dados"]["segunda_idade"]}'
        )
    elif resposta == 6:
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida.")