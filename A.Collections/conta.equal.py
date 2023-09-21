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


conta1 = ContaSalario(37)
conta2 = ContaSalario(37)

conta1 == conta2