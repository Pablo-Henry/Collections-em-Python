# Defaultdict() - utilizado para definir um valor padrão para um dicionário. Podemos passar um int para definir o valor padrão como 0
# Também podemos passar um valor para o construtor int, EX: int(15). !5 vira um valor padrão caso não tenha passado uma valor para a chave
from collections import defaultdict

dicionario = defaultdict(int)
dicionario["Pablo"]

print(list(dicionario))