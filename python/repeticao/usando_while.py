senha = 0 #valor inicial atribuido na senha

while senha != 123: #!= é diferente de, eu quando senha for diferente de 123, faça oque esta em baixo até acertar
    senha = int(input("tente acertar a senha"))

    if senha != 123:
        print("errou")
    else:
        print("malou ratao")