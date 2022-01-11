class ValorErradoError(Exception):
    pass


def testar():
    raise ValorErradoError('Errado')


try:
    testar()
except ValorErradoError as error:
    print(f'Erro: {error}')