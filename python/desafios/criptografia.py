senha = input("Digite a senha para ser criptografada:")
senha_invertida = (senha[::-1])

for escaner in senha_invertida:
    if escaner.lower() in "aeiou":
        print("*", end="")
    else:
        print(escaner.upper(), end="")