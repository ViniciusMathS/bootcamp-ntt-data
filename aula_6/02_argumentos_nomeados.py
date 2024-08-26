def salvar_carro(marca, modelo, ano):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}")

salvar_carro("Fiat", "Punto", 2014) 

salvar_carro(modelo="Jetta", marca="Volkswagen", ano=2018) # argumentos nomeados

salvar_carro(**{"ano":2017, "marca":"Ford", "modelo":"Ranger"}) # dicionario as chaves precisam ter os nomes dos argumentos da funcao