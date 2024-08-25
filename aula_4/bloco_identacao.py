def sacar(valor): # deixar 4 espaços para esquer a partir da linha que tem o dois pontos
    saldo=500

    if saldo >= valor:
        print("valor sacado!")

    print("Operção finalizada")

def depositar(valor):
    saldo = 500
    saldo += valor

sacar(1000)