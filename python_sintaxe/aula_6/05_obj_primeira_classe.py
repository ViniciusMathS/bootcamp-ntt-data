def somar(a, b):
    return a+b

def multiplicar(a, b):
    return a*b

def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado operação é = {resultado}")

exibir_resultado(10, 10, somar)

exibir_resultado(2, 2, multiplicar)

op = somar

print(op(2, 3))