from banco.clientes import Cliente
from banco.contas import ContaCorrente, ContaPoupanca

class BancoATM:
    def __init__(self):
        self.contas = {} # Agregação (o banco guarda contas, mas elas podem ser criadas fora)

    def menu(self):
        while True:
            print("\n--- CAIXA ELETRÔNICO ---")
            print("1 - Criar Conta")
            print("2 - Depositar")
            print("3 - Sacar")
            print("4 - Consultar Saldo")
            print("5 - Histórico")
            print("0 - Sair")
            
            opcao = input("Escolha uma opção: ")

            if opcao == "1":
                nome = input("Nome do cliente: ")
                cpf = input("CPF: ")
                num = input("Número da conta: ")
                tipo = input("Tipo (1-Corrente ou 2-Poupança): ")
                
                cliente = Cliente(nome, cpf)
                if tipo == "1":
                    self.contas[num] = ContaCorrente(num, cliente)
                else:
                    self.contas[num] = ContaPoupanca(num, cliente)
                print("Conta criada com sucesso!")

            elif opcao in ["2", "3", "4", "5"]:
                num = input("Informe o número da conta: ")
                conta = self.contas.get(num)
                
                if not conta:
                    print("Conta não encontrada!")
                    continue

                if opcao == "2":
                    val = float(input("Valor do depósito: "))
                    if conta.depositar(val): print("Sucesso!")
                elif opcao == "3":
                    val = float(input("Valor do saque: "))
                    if conta.sacar(val): print("Sucesso!")
                    else: print("Saldo insuficiente!")
                elif opcao == "4":
                    print(f"Saldo: R$ {conta.saldo:.2f}")
                elif opcao == "5":
                    conta.exibir_extrato()

            elif opcao == "0":
                break

if __name__ == "__main__":
    BancoATM().menu()
