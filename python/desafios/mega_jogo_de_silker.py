teste = True
while teste != False:
    print("Vamo Brincar com as palavras?")
    menu = """
    ==========================================

    (1) Tentar descobrir qual a senha do banco
    (2) Criptografar minha propria senha
    (SAIR) PARA SAIR
    
    ========================================== 
"""
    print(menu)
    primeira_pergunta = int(input("Oque vc prefere?"))
    if primeira_pergunta == 1:
        tentativas = 0
        descobriu = True
        senha = "123456"
        while descobriu != False:
            tentativa_de_senha = input("Qual voce acha que é a senha?")
            tentativas = tentativas + 1
            print(f"Voce tentou {tentativas} vezes")
            if tentativas == 1:
                print("DICA: A senha só tem numero")
            elif tentativas == 3:
                print("SE QUISER MAIS DICA DIGITE APELO")
            elif tentativa_de_senha == "APELO":
                print("12345_ ?")
            elif tentativa_de_senha == "123456":
                print("Cabo")
                descobriu = False
                teste = False
    if primeira_pergunta == 2:
        tentativa_segunda_pergunta = True
        senha = input("Qual senha voce quer criptografrar?")
        senha_intersa_primeira = (senha[::-1])
        for escaner in senha_intersa_primeira:
            if escaner.lower() in "aeiou":
                print("*",end="")
            elif escaner in "12345678910":
                print("-",end="")
            elif escaner in " ":
                print("+",end="")
            else:
                print(escaner.upper(),end="")
                teste = False
    if primeira_pergunta == 3:
        teste = False