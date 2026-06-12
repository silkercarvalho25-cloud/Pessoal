base_nome = input("Qual é o seu nome?:")
base2_idade = input("Qual é a sua idade?:")
base3_email = input("Qual é o seu email?:")

contatos = {
    "base":{"nome" : {base_nome}, 
            "idade" : {base2_idade}, 
            "email" : {base3_email}}
}

print("Oque vc quer saber de vc?")
resposta = input("""
nome
idade
email
""")

if resposta == "nome":
    print(contatos["base"]["nome"])