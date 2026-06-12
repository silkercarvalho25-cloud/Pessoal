contatos = {
    "pessoa1@gamil" : {"nome":"pessoa1@gmail", "idade":21}
}

print("="*40)

copia = contatos.copy() # criar uma copia
copia["pessoa1@gmail"] = {"nome" : "pessoaerrada@gmail"}
print(contatos["pessoa1@gamil"]["nome"])
print(copia["pessoa1@gmail"]["nome"])

print("="*40)
print(contatos.clear()) # apagar todo o dicionario