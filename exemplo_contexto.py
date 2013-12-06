class MeuContexto(object):
    def __init__(self, nome):
        self.nome = nome
    def __repr__(self):
        return 'MeuContexto(%r)' % self.nome
    def __enter__(self):
        print 'entrando em %r' % self
        return 'TRECO'
    def __exit__(self, type, value, traceback):
        print 'saindo de %r' % ((self, type, value, traceback),)

with MeuContexto('#1') as coisa:
	print '\tcoisa == %r' % coisa

