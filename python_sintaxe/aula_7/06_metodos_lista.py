lista = []

print("\nappend")
lista.append(1)
lista.append("Python") # adiciona um item no final da lista
lista.append([42, 30, 20])

print(f"lista: {lista}")

print("\ncopy")
lista_2 = lista.copy() # faz uma nova instancia da lista com os mesmos valores

print(lista is lista_2)
print(f"lista: {lista}")
print(f"lista_2: {lista_2}")

print("\nclear")
lista_2.clear() # exclui todos os itens da lista

print(f"lista: {lista}")
print(f"lista_2: {lista_2}")

print("\ncount")
cores = ["verde", "azul", "vermelho", "verde"]
print(cores.count("verde"))
print(cores.count("azul"))
print(cores.count("vermelho")) # conta quantas vezes o valor informado parecena lista

print("\nextend")
linguagens = ["python", "java"]
print(linguagens)
linguagens.extend(["swift", "c++", "sql"]) # faz a adição de varios itens no final da lista, espera um parametro iteravel
print(linguagens)

print("\nindex")
print(linguagens.index("java"))
print(linguagens.index("python")) # retorna o indice o da primeira ocorrencia do valor informado

print("\npop")    # lista vem organizada como uma pilha
linguagens.pop()  # remove o ultimo elemento adicionado na lista
linguagens.pop(3) # remove o indice informado no parametro
print(linguagens)

print("\nremove")
linguagens.remove("swift") # remove a primeira ocorrencia do valor informado da lista
print(linguagens)

print("\nreverse")
linguagens.reverse() # inverte a oredem da lista
print(linguagens)

print("\nsort")
animals = ["hippo","flamingo","snake","dog","koala","lion","aligator","eagle"]
animals.sort() # ordena na ordem crescente
print(animals) 
animals.sort(reverse=True) # ordena na ordem decrescente
print(animals) 
animals.sort(key=lambda x: len(x)) # ordena baseado em uma função, no caso da maior palavra para a menor
print(animals)
animals.sort(key=lambda x: len(x), reverse=True)
print(animals)

print("\nlen")
print(len(animals)) # mostra o tamanho da lista

print("\nsorted")
print(sorted(animals, key=lambda x: len(x))) # funcao sorted não altera o objeto
print(animals)