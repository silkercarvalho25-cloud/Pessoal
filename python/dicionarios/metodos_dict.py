familia = {
    "silker": {"nome_completo": "silker carvalho", "telefone" : "95165-1321"},
    "marcos": {"nome_completo":"marcos silva", "teleone":"98441-1232"},
    "felipe": {"nome_completo":"felipe da costa", "telefone":"95509-1325"},
    "neusa":{"telefone":"96229-1322"}
}

print("=" * 60)

copia = familia.copy() # Criar uma copia
copia["silker"] = {"nome_completo":"silker apenas"}

print(familia["silker"]["nome_completo"])
print(copia["silker"]["nome_completo"])

print("=" * 60)

copia_from = familia.fromkeys(["a mais um", "a mais dois"]) # criar chaves e add no dicionario
copia_from = familia.fromkeys(["a mais um", "a mais dois"], "conteudo",) # criar chaves e add no dicionario com valor
print(copia_from)
print(familia)

print("=" * 60)

print(familia.get("narco")) # procura se tem no dicionario "narco"
print(familia.get("narco", {"Nao achei"})) # caso nao achei "narco", retorne "{"nao achei"}"
print(familia.get("silker", {}))

print("=" * 60)

print(familia.keys()) # retona apenas as chaves dos dicionarios

print("=" * 60)

resultado = familia.pop("felipe") #remover uma chave a lista
print(resultado)

resultado = familia.pop("felipe", {}) #caso nao ache oque é pra remover, mostre {}
print(resultado) 


print("=" * 60)

resp = familia["silker"].setdefault("nome_completo","legal") #procura se tem alguma chave com o nome, se ja tiver, nao faz nada
resp = familia["silker"].setdefault("silker","legal") # se nao tiver ainda, adiciona ela
print(resp)
print(familia)

print("=" * 60)

familia["silker"].update({"nome_completo": "silker carvalho fidelles"}) # atualiza o dicionario
familia.update({"natalia":{"nome_completo": "natalida dos santos", "telefone":"98952-4562"}})

print(familia)

print("=" * 60)
print(familia.clear()) # Apagar os valores do dicionario    