from banco.clientes import Cliente # importa a classe Cliente do arquivo clientes
from banco.contas import ContaCorrente, ContaPoupanca # importa as classes ContaCorrente e ContaPoupanca do arquivo contas

class BancoATM:
    def __init__(self):
        self.contas = {} # Agregação (o banco guarda contas, mas elas podem ser criadas fora)

    def menu(self): # função do menu principal
        while True:
            print("\n--- CAIXA ELETRÔNICO ---")
            print("1 - Criar Conta")
            print("2 - Depositar")
            print("3 - Sacar")
            print("4 - Consultar Saldo")
            print("5 - Histórico")
            print("0 - Sair")
            
            opcao = input("Escolha uma opção: ")

            if opcao == "1": # opção de criar conta
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

                if opcao == "2": # opção de depositar
                    valor = float(input("Valor do depósito: "))
                    if conta.depositar(valor): print(f"Valor de {valor} depositado com sucesso!")
                elif opcao == "3": # opção de sacar
                    valor = float(input("Valor do saque: "))
                    if conta.sacar(valor): print(f"Valor de {valor} sacado com sucesso!")
                    else: print("Saldo insuficiente!")
                elif opcao == "4": # opção de consultar saldo
                    print(f"Saldo: R$ {conta.saldo:.2f}")
                elif opcao == "5": # opção de verificar o histórico
                    conta.exibir_extrato()

            elif opcao == "0": # opção de sair
                break

if __name__ == "__main__":
    BancoATM().menu()
