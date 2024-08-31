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

print(contatos["matheus@rosa.com"]["idade"])

extra = contatos["pedro@coelho.com"]["extra"]["valor"]

print(extra)

