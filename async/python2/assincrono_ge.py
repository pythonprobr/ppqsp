# coding: utf-8

from tornado import httpclient, ioloop, gen

from utilflags import ler_siglas, salvar, reportar, BASE_URL

qt_bytes = 0
qt_arqs = 0
conj_baixar = set()

@gen.engine
def processar(cliente, nome, numero):
    global qt_bytes, qt_arqs
    conj_baixar.add(nome)
    url = BASE_URL+nome
    print('\t\tbaixando %s' % nome)
    response = yield gen.Task(cliente.fetch, url)
    if response.error:
        print('Erro ao baixar %s: %r' %
              (nome, response.error))
        # XXX: como tratar erros neste caso?
        # cliente.fetch(response.request.url, XXX)
    else:
        qt_bytes += salvar(nome, response.body)
        qt_arqs += 1
        print '\t\t\t%3d\t%s --> salvo' % (numero, nome)
        conj_baixar.discard(nome)
        if not conj_baixar:
            ioloop.IOLoop.instance().stop()

def baixar(qtd):
    """ busca a quantidade ``qtd`` de bandeiras """

    cliente = httpclient.AsyncHTTPClient()

    for num, sigla in enumerate(ler_siglas(qtd), 1):
        nome = sigla + '-lgflag.gif'
        print '\t%3d\t%s' % (num, nome)
        processar(cliente, nome, num)

    print '*** antes do loop de eventos'
    ioloop.IOLoop.instance().start()
    print '*** depois do loop de eventos'

    return qt_bytes, qt_arqs

if __name__=='__main__':
    reportar(baixar)
