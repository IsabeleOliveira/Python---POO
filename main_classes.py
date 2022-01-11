from classes_intro import Pessoa

p1 = Pessoa('Luiz', 29)
p1.comer('Maçã')
p1.falar('Poo')
p1.parar_de_comer()
p1.falar('Poo')
p1.comer('alimento')
p2 = Pessoa('João', 32)
p2.comer('uva')
p2.falar('álgebra')
p2.parar_de_falar()
p2.comer('alimento')


print(p1.pegar_ano_nascimento())
print(p2.pegar_ano_nascimento())

