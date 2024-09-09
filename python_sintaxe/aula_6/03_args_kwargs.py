def exibir_poema(data_extenso, *args, **kwargs):
    texto = "\n".join(args)
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    print(mensagem)

exibir_poema(
    "Segunda-feira, 26 de Agosto de 2024",    # data_extenso sempre sera a primeira linha apenas quando
    "SE EU MORRESSE AMANHÃ",                  # *args todo o resto separado por virgula srea uma lista
    "Se eu morresse amanhã, viria ao menos",
    "Fechar meus olhos minha triste irmã",
    "Minha mãe de saudades morreria",
    "Se eu morresse amanhã!",
    autor = "Álvares de Azevedo"              # **kwargs apenas quando tiver argumentos nomeados será considerado
)