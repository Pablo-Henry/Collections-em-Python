# Criação de dicionário, um dicionário é constituído por uma chave(Primeiro elemento) e um valor(Segundo elemento)
aparicoes = {"Pablo": 888, "nomes": 1, "Henry": 4, "meu": 2, "TI": 777}

# Chamando o elemento Pablo para aparecer sua chave 888
print("Chave: ", aparicoes["Pablo"])


# Caso não tenha o elemento ADM no dicionário ira retornar 0
print(aparicoes.get("ADM", 0 ))

# Outra forma de criar um dicionario é utilizando a função Dict(), normalmente devemos utilizar a outra forma de criação
#  EX: teste = dict(Pablo = 888, TI = 777)

# Adicionando uma valor ao dicionário
aparicoes["Shrek"] = 1

# Substituindo um valor de um dicionário
aparicoes["Shrek"] = 2

# Removendo um valor de um Dicionário
del aparicoes["meu"]

# Mostra as chaves(Nomes)
for elementos in aparicoes:
    print(elementos)

# Mostra as Chaves(que são os nomes)
for elementos in aparicoes.keys():
    print(elementos)

# Mostra os valores(que são os números)
for elementos in aparicoes.values():
    print(elementos)

# Mostra as chaves e os valores
for elementos in aparicoes.items():
    print(elementos)

# Desempacotando os valores
for elementos, valores in aparicoes.items():
    print(elementos, "=", valores)

# List Compreshions com dicionários:
# Para cada chave em aparições, adicione Palavra antes
print([f"Palavra {chave}" for chave in aparicoes.keys()])

#Para cada valor em aparições, adicioe Valor antes
print([f"Key {valor}" for valor in aparicoes.values()])

# Para cada Palavra e Chave em aparicoes, adicione Palavra e Valor antes
print([f"Palavra {chave}, Valor {valor}" for chave, valor in aparicoes.items()])