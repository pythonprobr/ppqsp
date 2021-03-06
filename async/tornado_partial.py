# coding: utf-8

import functools

from tornado import httpclient, ioloop

from utilflags import ler_siglas, salvar, reportar, BASE_URL

qt_bytes = 0
qt_arqs = 0
conj_baixar = set()

def processar(nome, numero, response):
    global qt_bytes, qt_arqs
    if response.error:
        print('Erro: ', response.error)
        print('\tTentando de novo...', response.request.url)
        http_client.fetch(response.request.url, faz_processar(nome, numero))
    else:
        qt_bytes += salvar(nome, response.body)
        qt_arqs += 1
        print('\t\t\t%3d\t%s --> salvo' % (numero, nome))
        conj_baixar.discard(nome)
        if not conj_baixar:
            ioloop.IOLoop.instance().stop()

def baixar(qtd):
    """ busca a quantidade ``qtd`` de bandeiras """

    http_client = httpclient.AsyncHTTPClient()

    for num, sigla in enumerate(ler_siglas(qtd), 1):
        nome = sigla + '-lgflag.gif'
        print('\t%3d\t%s' % (num, nome))
        url = BASE_URL+nome
        conj_baixar.add(nome)
        proc = functools.partial(processar, nome, num)
        http_client.fetch(url, proc)

    ioloop.IOLoop.instance().start()
    return qt_bytes, qt_arqs

if __name__=='__main__':
    reportar(baixar)


