texto = input("informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end=" ")
else:
    print()
    print("Executa no final do laço")

for numero in range(11):   # numero tera os valores {0,1,2,3,4,5,6,7,8,9,10}
    print(numero, end=" ")

print()

for numero in range(0, 51, 5): # range pode receber 3 parametros
    print(numero, end=" ")     # numero inicial, numero final, intervalo