usuarios = [
    ("Guilherme", 12,2011),
("Pablo", 18,2004),
("Henry", 18,2004)
]

 # Exibe apenas a infomação passada no print()
for nome, idade, ano in usuarios:
    print(nome)


# Exibindo apenas o nome e ignorando o resto
for nome,_ , _  in usuarios:
    print(nome)