print("Voce é conta normal ou universitaria?")
resposta = str(input("Respaosta:"))
if resposta == "normal":
    total = 500
    saldo = float(input(f"Quanto vc quer sacar?, voce tem {total} no banco:"))
    if saldo <= total:
        print (f"vc sacou {saldo} e sobrou {total - saldo}")
elif resposta == "universitaria":
    total = 500
    saldo = float(input(f"Quanto vc quer sacar?, voce tem {total} no banco"))
    if saldo <= total:
        print (f"vc sacou {saldo} e sobrou {total - saldo}")
    else:
        print("Mas voce nem tem tudo issoKKKKKKKKKKKKKKKk")
else:
    print("Escreve direito pfvr")