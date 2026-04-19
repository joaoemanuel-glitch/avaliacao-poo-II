from datetime import datetime

class Operacao:
    def __init__(self, tipo, valor):
        self.__tipo = tipo
        self.__valor = valor
        self.__data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def __str__(self):
        return f"[{self.__data}] {self.__tipo}: R$ {self.__valor:.2f}"

class Historico:
    def __init__(self):
        self.__transacoes = [] # lista de transações criada internamente

    def adicionar_transacao(self, operacao):
        self.__transacoes.append(operacao) # adiciona uma operação na lista de transações

    def listar_historico(self):
        return self.__transacoes if self.__transacoes else ["Nenhuma operação realizada."]
