tupla = tuple() # tuplas são imutáveis

frutas = ("laranja", "uva", "pera",)

letras = tuple("python")

numeros = tuple([1,2,3,4])

pais = ("Brasil",)

print("\nacessando itens")
frutas[0] # laranja
frutas[2] # pera

frutas[-1] # pera
frutas[-3] # laranja

print("\ntupla alinhada")
matriz = (       # tuplas alinhadas
    (1, "a", 2),
    ("b", 3, 4),
    (6, 5, "c")
)

print(matriz[0]) # [1, "a", 2]
print(matriz[0][0]) # 1
print(matriz[0][-1]) # 2
print(matriz[-1][-1]) # "c"

print("\nfatiamento")
print(letras)
print(letras[2:])    # ["t", "h", "o", "n"]
print(letras[:2])    # ["p", "y"]
print(letras[1:3])   # ["y", "t"]
print(letras[0:3:2]) # ["p", "t"]
print(letras[::])    # ["p", "y", "t", "h", "o", "n"]
print(letras[::-1])  # ["n", "o", "h", "t", "y", "p"]

print("\niterar")
for item in frutas:
    print(item)

for indice, item in enumerate(frutas):
    print(f"{indice}: {item}")