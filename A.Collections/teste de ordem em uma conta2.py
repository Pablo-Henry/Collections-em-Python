class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0

    def __eq__(self, other):                                      # Equal: utilizado para verificar a igualdade dos objetos ou das classes
        if type(other) != ContaSalario:                           # Verifica se a classe é igual
            return False

        return self._codigo == other._codigo and self._saldo == other._saldo  #Verifica se o código e o saldo são iguais

    def deposita(self, valor):
        self._saldo += valor

    def __str__(self):
        return f'Código da Conta {self._codigo} - Saldo da Conta {self._saldo}'


conta1 =  ContaSalario(444)
conta1.deposita(1001)
conta2 =  ContaSalario(777)
conta2.deposita(1002)
conta3 =  ContaSalario(888)
conta3.deposita(1002)
conta4 = ContaSalario(999)
conta4.deposita(1008)

contas = [conta1, conta2, conta3]


 # Ordena as contas da maior para a menor pela quantidade que há no saldo - sem usar a função __lt__
from operator import attrgetter       # attrgetter - Utilizado para mostrar umj atributo encapsulado
for conta in sorted(contas, key=attrgetter("_saldo")):
    print(conta)











