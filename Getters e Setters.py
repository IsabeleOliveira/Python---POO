class Pessoa:
    def __init__(self, nome, sobrenome):
        self._nome = nome
        self._sobrenome = sobrenome

    """

    def __init__(self, nome):
        self._nome = nome

    """

    @property  # Um getter criado para pegar o parâmetro privado, da classe de inicialização
    def nome(self):
        return self._nome

    @nome.setter  # Setter do parâmetro privado (nome), criado para que possa ser alterado ou inserido algum valor
    def nome(self, nome):
        self._nome = nome

    """"@property  # Getter criado para pegar um sobrenome sem a necessidade de ter um setter
    def sobrenome(self):
        return 'Oliveira'
    """

    @property
    def sobrenome(self):
        return self._sobrenome


    @sobrenome.setter  # Setter do parâmetro privado (sobrenome),
    # criado para que possa ser alterado ou inserido algum valor
    def sobrenome(self, sobrenome):
        self._sobrenome = sobrenome



p1 = Pessoa('Isabele', 'Oliveira')
# p2 = Pessoa('Isabele')
print(p1.nome)
print(p1.sobrenome)
# print(p2.nome)
# print(p2.sobrenome)
