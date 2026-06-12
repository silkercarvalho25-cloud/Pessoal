def sacar(valor:float): #este float sendo uma coisa opcional
    saldo = 500 
    if saldo >= valor:
        print("valor sacado!!!")
    print("obrigado por confiar no nosso banco")

def depositar(valor):
    saldo = 500 #é necessario que ocorra a identação como se fosse paragrafos
    saldo += valor#dependendo de onde for a identação, ela esta para alguma parte do codigo

sacar(100)
depositar(20)