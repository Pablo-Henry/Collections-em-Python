usuarios_data_science = [15, 23, 56, 42]
usuarios_machine_learning = [18, 23, 88, 56]


# Coý(): utilizado para criar uma cópia de uma lista já criada e adicionar em outra
assistiram = usuarios_data_science.copy()

# Extend(): utilizado para adicionar itens de uma lista a outra
assistiram.extend(usuarios_machine_learning)

print(assistiram)


#Set():  Utilizado para a criação de conjuntos, utilizando o set é possível fazer com que uma valor não aparece duplicado
# O Set é utilizado apenas quando a ordem de exibição não é importante

set(assistiram)

# set([1, 2, 3])  ex de criação de um conjunto utilizando set

for usuario in set(assistiram):
    print(usuario)

# imprime os usuarios que estão nos dois conjuntos, não imprime valores duplicados por conta de que esta sendo utilizado um conjunto
# que é representado pelos colchetes {}
usuarios_data_science = {15, 23, 56, 42}
usuarios_machine_learning = {18, 23, 88, 56}

# a Barra invertida | pode ser utilizado como o operador Lógico ou
# Imprime os usuários da lista de machine learning e dos usuários do conjunto de data science sem que haja duplicidade
print(usuarios_machine_learning | usuarios_data_science)
