
class A:
    vc = 123


a1 = A()  #instância da classe
a2 = A()  #instância da classe

a1.vc = 321 #alterando somente uma instância da classe
A.vc = 432  #alterando todas as instâncias de classe

print(A.vc)
print(a2.vc)
print(a1.vc)
