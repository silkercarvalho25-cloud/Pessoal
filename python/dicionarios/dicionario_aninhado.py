contatos = {
    "silker@email.com" : {"nome":"silker", "telefone" : "9148-3286"},
    "pessoa1@email.com" : {"nome":"pessoa1", "telefone" : "95615-5610"},
    "pessoa2@gmail.com" : {"nome":"pessoa2", "telefone": "93204-6515"},
    "pessoa3@gmail.com" : {"nome" : "pessoa3", "telefone" : "9651-6214"},
    "teste" : "teste"
}

print(contatos["pessoa2@gmail.com"]["nome"])

print(contatos["pessoa3@gmail.com"]["telefone"])

for chave, valor in contatos.items():
    print(f"{valor}")