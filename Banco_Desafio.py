
class Banco:
    def __init__(self):
        self.agencias = [1111, 2222, 3333]
        self.clientes = []
        self.contas = []

    def inserir_clientes(self, clientes):
        self.clientes.append(clientes)

    def inserir_contas(self, conta):
        self.contas.append(conta)

    def autenticar(self, clientes):
        if clientes not in self.clientes:
            return False

        if clientes.conta not in self.contas:
            return False

        if clientes.conta.agencia not in self.agencias:
            return False

        return True