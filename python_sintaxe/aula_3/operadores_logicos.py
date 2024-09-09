print(True and False)
print(False and False)
print(True and True)    #operador 'and' retora verdadeiro somente se as duas condições forem verdadeiras

print(True or False)
print(True or True)
print(False or False)   #operador 'or' retora falso somente se as duas condições forem falsas

print(not(True))        #operador 'not' inverte o valor booleano

print("EXEMPLO EXPRESSÃO")
saldo = 1000
limite = 200
saque = 250
conta_especial = True

#expressões logicas são executadas da esquerda para a diraita, no caso de parenteses segue a regra da matematica

resultado = ((saldo >= saque) and (saque <= limite)) or ((saldo >= saque) and (conta_especial))
print(resultado)

print("EXEMPLO LISTA")
lista = []

#lista vazias são falsas, se tiverem um qualquer informaçao dentro delas elas serão verdadeiras

print(not lista)

lista.append(3)

print(not lista)