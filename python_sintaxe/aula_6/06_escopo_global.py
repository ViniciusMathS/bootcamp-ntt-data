salario = 2000

def salario_bonus(bonus, lista):
    global salario
    lista_aux = lista[:]
    lista_aux.append(2)
    print(f"Lista auxiliar: {lista_aux}")
    salario+=bonus
    return salario

lista = [1]

print(salario_bonus(500, lista))
print(lista)