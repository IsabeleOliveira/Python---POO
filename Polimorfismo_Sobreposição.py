"""
Polimorfismo é permitir que classes derivadas de uma SUPERCLASSE ter métodos iguais(de mesmos parâmetros)
mas possuir comportamentos diferentes.
"""

from abc import ABC, abstractmethod


class A(ABC):

    @abstractmethod
    def comer(self, msg):
        pass


class B(A):
    def comer(self, msg):
        print(f'B está comendo {msg}')


class C(A):
    def comer(self, msg):
        print(f'C está comendo {msg}')


b = B()
c = C()
b.comer('Chocolate')
c.comer('Outra coisa')

