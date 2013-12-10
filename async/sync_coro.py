import asyncio
import aiohttp

from utilflags import ler_siglas, salvar, reportar, BASE_URL


qt_bytes = 0
qt_arqs = 0

@asyncio.coroutine
def processar(nome, numero):
    global qt_bytes, qt_arqs
    url = BASE_URL+nome
    response = yield from aiohttp.request('GET', url)
    data = yield from response.read()
    qt_bytes += salvar(nome, data)
    qt_arqs += 1
    print('\t\t\t%3d\t%s --> salvo' % (numero, nome))

def baixar(qtd):
    """ busca a quantidade ``qtd`` de bandeiras """
    loop = asyncio.get_event_loop()

    for num, sigla in enumerate(ler_siglas(qtd), 1):
        nome = sigla + '-lgflag.gif'
        print('\t%3d\t%s' % (num, nome))
        loop.run_until_complete(processar(nome, num))

    return qt_bytes, qt_arqs

if __name__=='__main__':
    reportar(baixar)
