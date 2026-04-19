from banco.operacoes import Historico # importa a classe Historico do arquivo operacoes
from banco.operacoes import Operacao # importa a classe Operacao do arquivo operacoes

class Conta: # Classe base
    def __init__(self, numero, cliente):
        self._numero = numero
        self._cliente = cliente
        self._saldo = 0.0
        self.__historico = Historico() # Composição (o Histórico é criado dentro da Conta)

    @property
    def saldo(self):
        return self._saldo # retorna o saldo da conta

    def depositar(self, valor):
        if valor > 0: # se o valor for positivo
            self._saldo += valor # soma o valor depositado com o saldo
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
        if valor <= self._saldo: # se o valor for menor ou igual ao saldo
            self._saldo -= valor # extrai o valor sacado do saldo
            self._Conta__historico.adicionar_transacao(Operacao("Saque (CC)", valor))
            return True
        return False

class ContaPoupanca(Conta): # Subclasse
    def sacar(self, valor):
        if valor <= self._saldo: # se o valor for menor ou igual ao saldo
            self._saldo -= valor # extrai o valor sacado do saldo
            self._Conta__historico.adicionar_transacao(Operacao("Saque (CP)", valor))
            return True
        return False
