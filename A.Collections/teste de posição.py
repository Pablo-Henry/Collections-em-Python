# Mostra as idades e as posicões delas

idades = [12, 41, 32, 56, 45, 18, 88, 77, 28]

for i in range(len(idades)):
    print(f"Posição {i} - idade {idades[i]}")


#  Também mostra as idades e as posicões delas

print(list(range(len(idades))))  # utilizando o list() forçamos que haja a exibição das posições

print(list(enumerate(idades)))  # utilizando o list() com enumerate() forçamos que a haja a exibição da\ posições e o valor nas posições exibidas

for valor in enumerate(idades):
    print(valor)

# enumerate(): mostra a posição e o valor que esta na posição exibida


# Removendo os valores de dentro da tupla de exibição
for indice, idades in enumerate(idades):
    print(indice, "X",  idades)