import funcoes_banco as banco

lista_usuarios = []

menu = """
    =========== MENU ===========
     [1] Depositar
     [2] Sacar
     [3] Extrato
     [4] Cadastrar cliente
     [5] Cadastrar conta
     [0] Sair
    =========== MENU ===========
    => """

while True:

    operacao = int(input(menu))

    if operacao == 1:
        banco.depositar()
    elif operacao == 2:
        banco.sacar()
    elif operacao == 3:
        banco.exibir_extrato()
    elif operacao == 4:
        banco.cadastrar_usuario(lista_usuarios)
    elif operacao == 5:
        banco.cadastrar_conta()
    elif operacao == 0:
        print( "Operação finaliza.")
        print(lista_usuarios)
        break
    else:
        print(" Informe uma operção valida.")