contatos = {
    "matheus@rosa.com" : {
        "nome" : "matheus da rosa",
        "idade" : 19
    },
    "pedro@coelho.com" : {
        "nome" : "pedro coelho",
        "idade" : 12
    }
}

print("\ncopy")
contatos_copia = contatos.copy()
print(contatos_copia)

print("\nclear")
contatos_copia.clear()
print(contatos_copia)

print("\nfromkeys")
pessoa = dict.fromkeys(["nome", "fone", "email"], "-") # cria um dicionario com uma lista de chaves informadas e com um valor padrão
print(pessoa)

print("\nget")
# contatos["chave"] # KeyError
resultado=contatos.get("chave") # retorna o  valor da chave ou None se a chave não existir
resultado=contatos.get("chave", False) # retorna um valor default caso a chave não exista
print(resultado)
resultado=contatos.get("pedro@coelho.com", {}).get("idade", {})  
print(resultado)

print("\nitems")
itens = contatos.items() # retorna uma lista de tuplas, cada tupla possui a chave e o valor
print(itens)

print("\nkeys")
chaves = contatos.keys() # retorna uma lista com as chaves do dicionario
print(chaves)

print("\npop")
print(contatos.pop("chave", "Não encontrado")) # remove e retorna o valor removido do dicionario, caso a chave não exista causara KeyError, o sengundo parametro é um retorno default

print("\npopitem")
print(pessoa.popitem()) # remove o ultimo item adicionado no dicionario, caso o dicionario esteja vazio causa um KeyError

print("\nsetdefault")
pessoa.setdefault("nome", "vinicius") # adiciona a chave informada com o valor informado, caso a chave ja exista ela não é alterada
pessoa.setdefault("idade", 24)
print(pessoa)

print("\nupdate")
contatos.update({"pedro@coelho.com":{"nome":"coelhinho", "idade":13}})    # atualiza a chave informada com um novo valor
contatos.update({"vinicius@matheus.com":{"nome":"vinicius", "idade":24}}) # caso a chave não exista ela é criada com o valor informado
print(contatos)

print("\nvalues")
valores = contatos.values() # retorna uma lista com os valores do dicionario
print(valores)

print("\nin")
print("matheus@rosa.com" in contatos) # verifica se a chave existe no dicionario
print("nome" in contatos) 
print("nome" in contatos["pedro@coelho.com"])
print("chave" in contatos["matheus@rosa.com"])

print("\ndel")
del contatos["pedro@coelho.com"]["idade"] # deleta a chave informada 
del contatos["vinicius@matheus.com"]      # caso não exista causa um KeyError
print(contatos)
del contatos # apaga o dicionario inteiro

def filtrar_por_valor(products : list, min_value : float, max_value : float) -> list:
    return [product for product in products if product['preco'] >= min_value and product['preco'] <= max_value]
