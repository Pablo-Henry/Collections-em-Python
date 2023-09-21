from collections import defaultdict

meu_texto = "Meu nome é Pablo e meu nome também é Henry"
# Lower() - deixa todas as palavras com as letras minúsculas
meu_texto = meu_texto.lower()

aparicoes = defaultdict(int)

# Conta quantas vezes a palavra apareceu no texto
for palavra in meu_texto.split():
# Busca e adiciona +1 ao valor da palavra, caso o valor seja 0 vira 1 , se for 7 vira 8 e assim sucessivamente
    aparicoes[palavra] += 1

# Utilizando Dict() conseguimos fazer corretamente o print
# Se utilizar List(), não irá imprimir a quantidade de palavras, vai imprimir somente as palavras
print(dict(aparicoes))


