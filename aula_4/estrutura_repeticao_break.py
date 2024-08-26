while True:
    numero = int(input("informe um numero: "))

    if numero == 11: 
        continue # continua o loop sem executar o código abaixo dele
    if numero == 10:
        break # para o loop sem executar o código abaixo dele

    print(numero)

for numero in range(100):
    if numero % 2 == 0:
        continue
    print(numero)