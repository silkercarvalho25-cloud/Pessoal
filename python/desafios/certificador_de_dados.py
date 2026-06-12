
banco_de_dados = {
    "silker": {"nome" :"silker", "senha":"123456"},
    "ssamira": {"nome": "samira" , "senha": "789456"}  
}
resposta = input("Qual no voce quer bota no banco de dados?:")
analista = banco_de_dados.get(resposta)
if analista:
    print(f"Conta achada {banco_de_dados["silker"]}")
else:
    print("Nao foi possivel achar a conta")