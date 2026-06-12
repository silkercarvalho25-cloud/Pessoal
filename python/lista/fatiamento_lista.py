lista = ["p", "y", "t", "h", "o", "n"]

# Fatiar do índice 2 até o final
print(lista[2:])    # Saída: ["t", "h", "o", "n"]

# Fatiar do início até o índice 2 (exclusivo)
print(lista[:2])    # Saída: ["p", "y"]

# Fatiar do índice 1 até o 3 (exclusivo)
print(lista[1:3])   # Saída: ["y", "t"]

# Fatiar do índice 0 ao 3, com passo 2
print(lista[0:3:2]) # Saída: ["p", "t"]

# Criar uma cópia da lista inteira
print(lista[::])   # Saída: ["p", "y", "t", "h", "o", "n"]

# Inverter a lista
print(lista[::-1])  # Saída: ["n", "o", "h", "t", "y", "p"]