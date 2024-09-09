eu = {
    "nome" : "Vinicius Matheus",
    "idade" : 24,
    "profissao" : "Estudante",
    "linguagem" : "Python"
}

print("Nome: %s, Idade: %d" %(eu["nome"], eu["idade"]))
print("Nome: {}, Idade: {}" .format(eu["nome"], eu["idade"]))
print("Nome: {0}, Idade: {1}, NomeIdade: {0} {1}" .format(eu["nome"], eu["idade"]))
print("Nome: {name}, Idade: {age}, NomeIdade: {name} {age}" .format(name=eu["nome"], age=eu["idade"]))
print("Nome: {nome}, Idade: {idade}" .format(**eu)) # para dicts passando o nome da chave desejada

# print f: 

print(f"Ola, meu nome é {eu['nome']}, tenho {eu['idade']} anos de idade, sou {eu['profissao']} e estudo a lingugem {eu['linguagem']}.")

PI = 3.14159

print(f"Valor de pi: {PI:.3f}") # numero de casas decimais com arredondamento

print(f"Valor de pi: {PI:10.2f}") # numero de espaço antes de exibir o numero
