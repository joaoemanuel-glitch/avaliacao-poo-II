from datetime import datetime # importa a biblioteca datetime que vai ser usada para mostrar o horário e o dia das operações realizadas

class Operacao:
    def __init__(self, tipo, valor):
        self.__tipo = tipo
        self.__valor = valor
        self.__data = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    def __str__(self):
        return f"[{self.__data}] {self.__tipo}: R$ {self.__valor:.2f}"
        retorna a data e a hora da operação, o tipo de operação e o valor que foi usado na operação

class Historico:
    def __init__(self):
        self.__transacoes = [] # lista de transações criada internamente

    def adicionar_transacao(self, operacao):
        self.__transacoes.append(operacao) # adiciona uma operação na lista de transações

    def listar_historico(self):
        return self.__transacoes if self.__transacoes else ["Nenhuma operação realizada."]
        # se houver, lista o histórico de transações, caso contrário, informa que não há nenhuma operação realizada
