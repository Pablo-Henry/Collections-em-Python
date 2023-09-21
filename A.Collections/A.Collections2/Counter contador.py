# Função Counter() - utilizado para contar a quantidade de vezes que um elemento aparece

from collections import Counter

meu_texto = "Meu nome é Pablo e meu nome também é Henry"

aparicoes = Counter(meu_texto.split())

print(dict(aparicoes))
