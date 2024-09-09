def calcular_total(numeros):
    return sum(numeros)

def achar_sucessor_antecessor(numero):
    antecessor = numero -1
    sucessor = numero + 1
    return antecessor, sucessor

def func_3():
    print("Olá mundo!")

print(calcular_total([10, 20, 30])) # 60
print(achar_sucessor_antecessor(10)) # (9, 10)
print(func_3()) # executa a função e depois mostra None 