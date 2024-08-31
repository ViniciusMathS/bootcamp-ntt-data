contatos = {
    "matheus@rosa.com" : {
        "nome" : "matheus da rosa",
        "idade" : 19
    },
    "pedro@coelho.com" : {
        "nome" : "pedro coelho",
        "idade" : 19,
        "extra" : {
            "valor" : 1
        }
    }
}

for chave, valor in contatos.items():
    print(f"{chave} : {valor}")