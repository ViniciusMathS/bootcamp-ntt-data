from datetime import datetime

def is_usuario_existe(lsita_usuarios : list, cpf : str):
    for usuario in lsita_usuarios:
        if usuario['cpf'] == cpf:
            return True
    return False

def gerar_endereco():
    logradouro = input()
    numero = input()
    bairro = input()
    cidade = input()
    estado = input()
    return f"{logradouro}, {numero} - {bairro} - {cidade}/{estado}"

def gerar_data_nascimento():
    dia = int(input("Informe o dia de nascimento: "))
    mes = int(input("Informe o mês de nascimento: "))
    ano = int(input("Informe o mês de nascimento: "))
    return datetime(ano, mes, dia).date().strftime("%d/%m/%Y")

def depositar():
    pass

def sacar():
    pass

def exibir_extrato():
    pass

def cadastrar_usuario(lista_usuarios : list):
    usuario = {}
    usuario['cpf'] = input("Inform o CPF do cliente: ")
    if is_usuario_existe(lista_usuarios, usuario['cpf']):
        print("\nO CPF informado já esta cadastrado.")
    else:
        usuario['nome'] = input("Informe o nome completo do cliente: ")
        usuario['data_nascimento'] = gerar_data_nascimento()
        usuario['endereco'] = gerar_endereco()
        lista_usuarios.append(usuario) 
    
def cadastrar_conta():
    pass
