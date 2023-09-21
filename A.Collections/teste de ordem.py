idades = [12, 41, 32, 56, 45, 18, 88, 77, 28]

# Organiza a lista do menor para o maior
print(sorted(idades))

# Organiza a lista do maior para o menor - Não altera a variável que possuí a lista ou seja não altera a lista original
print(sorted(idades, reverse=True))

print(list(reversed(sorted(idades))))   # Tembém organiza a lista do maior para o menor

# Inverte a ordem da lista
print(list(reversed(idades)))

# idades.sort() - organiza a lista alterando sua ordem diretamente na variável que possuí a lista - muda a lista original

# idades.sort()
