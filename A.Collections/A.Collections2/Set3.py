usuarios = {1,5,23,45,72,65,88}

# add(): adiciona um novo item ao conjunto
usuarios.add(888)
print(usuarios)
# Frozenset(): congela o conjunto bloqueando que haja alterações no conjunto
usuarios = frozenset(usuarios)



meu_texto = "Meu nome é Pablo e meu nome também é Henry"
# Split(): remove os espaços do texto
print(meu_texto.split())

# Adiciona o texto a um conjunto
print(set(meu_texto.split()))


