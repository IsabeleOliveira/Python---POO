from Banco_Desafio import Banco
from Clientes_Desafio import Cliente
from Contas_Desafio import ContaCorrente, ContaPoupanca

banco = Banco()

cliente1 = Cliente('Isabele', 30)
cliente2 = Cliente('Maria', 18)
cliente3 = Cliente('João', 50)

conta1 = ContaPoupanca(1111, 254136, 0)
conta2 = ContaCorrente(2222, 254137, 0)
conta3 = ContaPoupanca(1212, 254138, 0)


cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)
cliente3.inserir_conta(conta3)

banco.inserir_clientes(cliente1)
banco.inserir_contas(conta1)

banco.inserir_clientes(cliente2)
banco.inserir_contas(conta2)

banco.inserir_clientes(cliente3)
banco.inserir_contas(conta3)

if banco.autenticar(cliente1):
    cliente1.conta.depositar(0)
    cliente1.conta.sacar(20)
else:
    print('Cliente não autenticado.')

print('Hora de verificar autenticação')

if banco.autenticar(cliente2):
    cliente2.conta.depositar(0)
    cliente2.conta.sacar(20)
else:
    print('Cliente não autenticado.')

if banco.autenticar(cliente3):
    cliente3.conta.depositar(50)
    cliente3.conta.sacar(10)
else:
    print('Cliente não autenticado.')