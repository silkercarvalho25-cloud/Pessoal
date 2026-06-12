tentativas = 0
verificador = False
print("DIGITE O USUARIO E SENHA PARA ENTRAR, 3 TENTATIVAS SAO TOLERAVEIS")
while verificador != True:
    usuario = "silker"
    senha = "123"
    tentativas = tentativas + 1
    pergunta_usuario = input("Digite o nome de usuario:")
    pergunta_senha = input("Digite a senha de usuario:")
    if pergunta_usuario != usuario and pergunta_senha != senha:
        print("USUARIO E SENHA ERRADOS")
        print(f"Voce tentou {tentativas} vezes")
        if tentativas == 3:
            print("VOCE EXCEDEU O NUMERO DE TENTATIVAS, ACESSO NEGADO!")
            verificador = True
    elif pergunta_usuario == usuario and pergunta_senha != senha:
        print("SENHA ERRADA")
        print(f"Voce tentou {tentativas} vezes")
        if tentativas == 3:
            print("VOCE EXCEDEU O NUMERO DE TENTATIVAS, ACESSO NEGADO!")
            verificador = True
    elif pergunta_usuario != usuario and pergunta_senha == senha:
        print("USUARIO ERRADO")
        print(f"Voce tentou {tentativas} vezes")
        if tentativas == 3:
            print("VOCE EXCEDEU O NUMERO DE TENTATIVAS, ACESSO NEGADO!")
            verificador = True
    else:
        print("ACESSO LIBERADO!")
        verificador = True