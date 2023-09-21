# Criação de conta utilizando Polimorfismo e Herança

from abc import ABCMeta, abstractmethod   #Força um erro em uma classe que não possuí parâmetros, o erro acontece
                                          #assim que a uma tentativa de instânciar um objeto que vem da classe que
                                          #não possuí parâmetros
class Conta(metaclass=ABCMeta):

    def __init__(self, codigo):
        self._codigo =  codigo
        self._saldo = 0

    def deposita(self, valor):
        self._saldo += valor

    @abstractmethod
    def passa_o_mes(self):
        pass

    def __str__(self):
        return f"Código da Conta: {self._codigo} - Saldo da Conta: {self._saldo}"

class ContaCorrente(Conta):

    def passa_o_mes(self):
        self._saldo -= 2

class ContaPoupanca(Conta):

    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

class ContaInvestimentos(Conta):          #exemplo de classe que retorna erro por falta de parâmetros
    pass                                  #exemplo de instância: conta = ContaInvestimento(888) - Retorna um erro

conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta16.passa_o_mes()
print(conta16)

conta17 = ContaPoupanca(17)
conta17.deposita(1000)
conta17.passa_o_mes()
print(conta17)

contas = [conta16, conta17]

for conta in contas:
    conta.passa_o_mes()                         #Duck Typing
    print(conta)

