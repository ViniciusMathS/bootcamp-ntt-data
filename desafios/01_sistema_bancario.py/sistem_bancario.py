extrato = ""
saldo = 0
withdraw_rate = 0

def is_valid_withdraw(withdraw_value : float):
    global withdraw_rate, saldo
    WITHDRAW_RATE_LIMIT = 3
    WITHDRAW_VALUE_LIMIT = 500.00
    if withdraw_value <= 0:
        erro_msg = "\n Operação invalida.\n O valor do saque deve ser maior que zero."
        return False, erro_msg
    if withdraw_rate == WITHDRAW_RATE_LIMIT or withdraw_value > WITHDRAW_VALUE_LIMIT:
        erro_msg = "\n Operação invalida.\n Quantidade ou limite de saque excedido."
        return False, erro_msg
    elif saldo < withdraw_value:
        erro_msg = "\n Operação invalida.\n Saldo insuficiente."
        return False, erro_msg
    return True, "\n Saque efetuado"
    
def withdraw(withdraw_value : float):
    global withdraw_rate, saldo, extrato
    saldo -= withdraw_value
    withdraw_rate += 1
    extrato += f" Saque: R${withdraw_value}\n"

def is_valid_dposit(deposit_value : float):
    if deposit_value <= 0:
        erro_msg = "\n Operação invalida.\n O valor do depósito deve ser maior que zero."
        return False, erro_msg
    return True, "\n Depósito efetuado" 

def deposit(deposit_value : float):
    global saldo, extrato
    saldo += deposit_value
    extrato += f" Depósito: R${deposit_value}\n"

def show_bank_statement():
    global extrato, saldo
    if len(extrato) == 0:
        print("\n Não foram realizadas movimentações.")
    else:
        print(f"\n{extrato} Saldo:{saldo}")

while True:
    print(
    """
    ====== MENU ======
     [1] Depositar
     [2] Sacar
     [3] Extrato
     [0] Sair
    ====== MENU ======
    """
    )

    option = int(input(" Informe a operação que deseja realizar: "))

    if option == 1:
        deposit_value = round(float(input("\n Informe o valor que deseja depositar: ")), 2)
        valid, msg = is_valid_dposit(deposit_value)
        
        if valid:
            deposit(deposit_value)
        print(msg)

    elif option == 2:
        withdraw_value = round(float(input("\n Informe o valor que deseja sacar: ")), 2)
        valid, msg = is_valid_withdraw(withdraw_value)

        if valid:
            withdraw(withdraw_value)
        print(msg)

    elif option == 3:
        show_bank_statement()

    elif option == 0:
        print("\n Operação finalizada.\n Tenha um bom dia.")
        break;
    
    else:
        print("\n Opção invalida.\n Por favor informe uma opção existente.")