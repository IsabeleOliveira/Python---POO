from contextlib import contextmanager

@contextmanager
def abrir(arquivo, modo):
    try:
        print('Abrindo arquivo')
        arquivo = open(arquivo, modo)
        yield arquivo
    finally:
        print('Fechando arquivo')
        arquivo.close()


with abrir('abcdeful.txt', 'w') as arquivo:
    arquivo.write('Ola\n')
    arquivo.write('usuario\n')
    arquivo.write('Seja Bem Vindo')


