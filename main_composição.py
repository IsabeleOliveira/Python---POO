from composição import Cliente

cliente1 = Cliente('Luiz', 32)
cliente1.inserir_endereco('Belo Horizonte', 'MG')
print(cliente1.nome)
cliente1.lista_enderecos()
del cliente1
print()

cliente2 = Cliente('Maria', 55)
cliente2.inserir_endereco('Salvador', 'BA')
print(cliente2.nome)
cliente2.lista_enderecos()
print()

cliente3 = Cliente('João', 19)
cliente3.inserir_endereco('São Paulo', 'SP')
print(cliente3.nome)
cliente3.lista_enderecos()
print()