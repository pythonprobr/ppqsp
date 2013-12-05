========================
Exemplo variavel local
========================

	>>> def f(a):
	...    print a
	...    print b
	...
	>>> b = 2
	>>> f(1)
	1
	2
	>>> def g(a):
	...    print a
	...    b = 20
	...    print b
	...
	>>> g(1)
	1
	20
	>>> def h(a):
	...    print a
	...    print b
	...    b = 20
	...
	>>> h(1)
	1
	Traceback (most recent call last):
	  File "<stdin>", line 1, in <module>
	  File "<stdin>", line 3, in h
	UnboundLocalError: local variable 'b' referenced before assignment
