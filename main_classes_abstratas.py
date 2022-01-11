from Classes_abstratas.conta_poupanca import ContaPoupanca
from Classes_abstratas.conta_corrente import ContaCorrente

conta = ContaPoupanca(1111, 2222, 0)
conta.depositar(10)
conta.sacar(5)
conta.sacar(5)
conta.sacar(1)

conta_corrente = ContaCorrente(1111, 3333, 0, 500)
conta_corrente.depositar(100)
conta_corrente.sacar(250)
conta_corrente.sacar(500)
conta_corrente.depositar(1000)