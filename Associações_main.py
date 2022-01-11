from Associações import Escritor
from Associações import Caneta
from Associações import MaquinaDeEscrever

escritor = Escritor('Isabele')
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()


#Associação

escritor.ferramenta = caneta
escritor.ferramenta.escrever()

escritor.ferramenta = maquina
escritor.ferramenta.escrever()

del escritor
print(caneta.marca)
maquina.escrever()