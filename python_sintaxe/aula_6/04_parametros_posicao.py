def criar_carro(modelo, ano, placa, /, marca, motor, *,combustivel): # os parametros antes da barra devem        # depois do asteristico devem 
    print(modelo, ano, placa, marca, motor, combustivel)             # ser passados por posição obrigatóriamente # ser passados nomeados obrigatóriamente
                                                                    
criar_carro("Palio", 1999, "ABC-1234", marca="FIAT", motor=1.8, combustivel="Gasolina") # valido

criar_carro("Palio", 1999, "ABC-1234", "FIAT", 1.8, combustivel="Gasolina") # valido

criar_carro("Palio", 1999, "ABC-1234", "FIAT", 1.8, "Gasolina") # invalido

criar_carro(ano=1999, modelo="Palio", placa="ABC-1234",marca="FIAT", motor=1.8, combustivel="Gasolina") # invalido
