# avaliacao-poo-II

# Sistema de Caixa Eletrônico (ATM) - POO em Python

Este projeto é uma simulação de um sistema bancário desenvolvido como atividade prática para a disciplina de Programação Orientada a Objetos. O objetivo é aplicar conceitos fundamentais de POO ao gerenciar contas e operações financeiras.

## Funcionalidades
- **Criação de Contas:** Cria Contas Corrente e Contas Poupança.
- **Operações Financeiras:** Depósitos e saques com validação de saldo.
- **Consulta de Saldo:** Verifica o saldo disponível.
- **Histórico de Operações:** Registro de todas as operações realizadas com data e hora de realização.

## Conceitos de POO Aplicados
O projeto foi estruturado utilizando os seguintes pilares:
1. **Pacotes:** Organização em pastas e módulos.
2. **Classes e Objetos:** Representação de Clientes, Contas e Operações.
3. **Herança:** As subclasse "ContaCorrente" e "ContaPoupanca" herdam da classe base "Conta".
4. **Polimorfismo:** O método "sacar()" é sobrescrito nas subclasses "ContaCorrente" e "ContaPoupanca".
5. **Encapsulamento:** Uso de atributos privados (__) e protegidos (_) para segurança dos dados.
6. **Agregação:** A classe "BancoATM" gerencia múltiplos objetos de contas.
7. **Composição:** A classe "Conta" possui um "Historico", que não existe sem a conta.
