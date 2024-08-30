conjuto = set([1, 1, 2, 3, 3, 2, 4, 2, 5]) # elimina as duplicações 
print(conjuto) 
print(set("arara")) # elimina as letras repitidas

tupla = ("palio", "gol", "uno", "palio",)
print(set(tupla))

linguagens = {"python", "java", "swift", "python"}
print(linguagens)

print("\nacessando dados de conjuntos")
numeros = {1,2,3,2}
numeros = list(numeros) # para acessar os dados de um conjunto é nescessario convertelo para lista
print(numeros[2])

print("\niterar")
for linguagem in linguagens:
    print(linguagem)

for indice, linguagem in enumerate(linguagens):
    print(f"{indice}: {linguagem}")



