from banco.operacoes import Historico
from banco.operacoes import Operacao

class Conta: # Classe base
    def __init__(self, numero, cliente):
        self._numero = numero
        self._cliente = cliente
        self._saldo = 0.0
        self.__historico = Historico() # Composição (o Histórico é criado dentro da Conta)

    @property
    def saldo(self):
        return self._saldo

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            self.__historico.adicionar_transacao(Operacao("Depósito", valor))
            return True
        return False

    def sacar(self, valor):
        # Esse método vai ser escrito novamente nas subclasses usando polimorfismo
        pass

    def exibir_extrato(self):
        print(f"\n--- Extrato Conta {self._numero} ---")
        for t in self.__historico.listar_historico():
            print(t)
        print(f"Saldo Atual: R$ {self._saldo:.2f}")

class ContaCorrente(Conta): # Subclasse
    def sacar(self, valor):
        taxa = 2.00  # Exemplo de regra diferente para CC
        if valor + taxa <= self._saldo:
            self._saldo -= (valor + taxa)
            self._Conta__historico.adicionar_transacao(Operacao("Saque (CC)", valor))
            return True
        return False

class ContaPoupanca(Conta): # Subclasse
    def sacar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
            self._Conta__historico.adicionar_transacao(Operacao("Saque (CP)", valor))
            return True
        return False
