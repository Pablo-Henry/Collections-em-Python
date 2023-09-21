meu_texto = "Meu nome é Pablo e meu nome também é Henry"
# Lower() - deixa todas as palavras com as letras minúsculas
meu_texto = meu_texto.lower()

aparicoes = {}


# Conta quantas vezes a palavra apareceu no texto
for palavra in meu_texto.split():
# Busca a palavra caso ela estaja lá retorna o seu valor, caso não não esteja retorna 0
    ate_agora = aparicoes.get(palavra, 0)
# Adiciona +1 ao valor da palavra, caso o valor seja 0 vira 1 , se for 7 vira 8 e assim sucessivamente
    aparicoes[palavra] = ate_agora + 1

print(aparicoes)

########################################################################################################################


# Outra forma de fazer o contado de palavras utilizando o defaultdict
# Utilizando defaultdict não precisamos mais de utilizar o get(), pois definimos um valor padrão, zero

from collections import defaultdict

meu_texto = "Meu nome é Pablo e meu nome também é Henry"
# Lower() - deixa todas as palavras com as letras minúsculas
meu_texto = meu_texto.lower()

aparicoes = defaultdict(int)


# Conta quantas vezes a palavra apareceu no texto
for palavra in meu_texto.split():
# Busca a palavra caso ela estaja lá retorna o seu valor, caso não não esteja retorna 0
    ate_agora = aparicoes[palavra]
# Adiciona +1 ao valor da palavra, caso o valor seja 0 vira 1 , se for 7 vira 8 e assim sucessivamente
    aparicoes[palavra] = ate_agora + 1

print(dict(aparicoes))


