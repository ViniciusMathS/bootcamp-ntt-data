conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}
conjunto_c = {1, 2, 3, 4, 5}
conjunto_d = {0, -1, -2, -3}

print("\nunion")
print(conjunto_a.union(conjunto_b)) # {1, 2, 3, 4}

print("\intersection")
print(conjunto_a.intersection(conjunto_b)) # {2, 3}

print("\ndifference")
print(conjunto_a.difference(conjunto_b)) # {1}
print(conjunto_b.difference(conjunto_a)) # {4}

print("\nsymetric_difference")
print(conjunto_a.symmetric_difference(conjunto_b)) # {1, 4}

print("\nissubset")
print(conjunto_a.issubset(conjunto_b)) # verifica se um conjunto esta contido dentro de outro
print(conjunto_a.issubset(conjunto_c))
print(conjunto_b.issubset(conjunto_c))

print("\nissuperset")
print(conjunto_c.issuperset(conjunto_a)) # verifica se um conjunto contem outro
print(conjunto_b.issuperset(conjunto_a))

print("\nisdisjoint")
print(conjunto_a.isdisjoint(conjunto_b)) # verifica se os conjuntos não possuem elementos em comum
print(conjunto_a.isdisjoint(conjunto_d))

print("\nadd")
conjunto_d.add(-4)  # adiciona o elemento ao conjunto se ele não existir no conjunto
conjunto_d.add(-16)
conjunto_d.add(-4)
print(conjunto_d)

print("\nclear")
conjunto_d.clear() # exclui todos os itens do conjunto
print(conjunto_d)

print("\ncopy")
aux = conjunto_a.copy() # cria um copia do conjunto
print(aux)

print("\ndiscard")
conjunto_c.discard(5)  # descarta o elemento informado do conjunto, se o elemento existir
conjunto_c.discard(10)
print(conjunto_c)

print("\npop")
print(aux) # {1, 2, 3}
aux.pop()  # elimina o primeiro elemento do conjunto
print(aux) # {2, 3}

print("\nremove")
aux.remove(3) # remove o elemento informado
aux.remove(2) # ocorre um erro se passar um item que não existe no conjunto 
print(aux)

print("\nlen")
print(len(conjunto_c)) # retorna o tamanho do conjunto

print("\nin")
print(1 in conjunto_c)
print(20 in conjunto_c) # verifica se um numero esta contido no conjunto