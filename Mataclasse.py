"""
Classes que criam classes.
type é uma metaclasse
"""


class Meta(type):
    def __new__(mcs, name, bases, namespace):
        if name == 'A':
            return type.__new__(mcs, name, bases, namespace)

        if 'attr_classe' in namespace:  # impedir que outras classes subescrevam
            del namespace['attr_classe']

        return type.__new__(mcs, name, bases, namespace)


class A(metaclass=Meta):
    attr_classe = 'Valor A'


class B(A):
    attr_classe = 'Valor B'


b = B()
print(b.attr_classe)


""" Outra forma de criar uma classe """

A = type('A', (), {'attr': 'Olá Mundo!'})

a = A()
print(a.attr)