class A:
    pass

class B(A): # Classe 'B' herda atributos e comportamentos da class 'A'
    pass

class C(B): # Classe 'C' herda atributos e comportamentos da class 'B' e 'A', pois 'B' herda de 'A'. (Herança Simples)
    pass

class X:
    pass

class Y:
    pass

class Z(X, Y): # Classe 'Z' herda atributos e comportamentos da class 'X' e 'Y', porem 'Y' não herda de 'X'. (Herança Multipla)
    pass
