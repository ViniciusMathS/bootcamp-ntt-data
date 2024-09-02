from datetime import datetime

WITHDRAW_VALUE_LIMIT = 500.00
TRANSACTION_RATE_LIMIT = 10
extrato = []
saldo = 0

def is_on_daily_transaction_limit() -> bool:
    global extrato, TRANSACTION_RATE_LIMIT
    today = datetime.today().date()
    today_transaxtions = [x for x in extrato if datetime.strptime(x['data'], "%d/%m/%Y %H:%M:%S").date() == today]
    if len(today_transaxtions) >= 10:
        return True
    return False

def is_valid_withdraw(withdraw_value : float):
    global saldo, WITHDRAW_VALUE_LIMIT
    if withdraw_value <= 0:
        erro_msg = "\n Operação invalida.\n O valor do saque deve ser maior que zero."
        return False, erro_msg
    elif withdraw_value > WITHDRAW_VALUE_LIMIT:
        erro_msg = "\n Operação invalida.\n Valor limite de saque excedido."
        return False, erro_msg
    elif is_on_daily_transaction_limit():
        erro_msg = "\n Operação invalida.\n Limite de transações excedido."
        return False, erro_msg
    elif saldo < withdraw_value:
        erro_msg = "\n Operação invalida.\n Saldo insuficiente."
        return False, erro_msg
    return True, "\n Saque efetuado"
    
def withdraw(withdraw_value : float):
    global saldo, extrato
    saldo -= withdraw_value
    withdraw_date = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    transaction={'data':withdraw_date, 'tipo': "Saque", 'valor':withdraw_value}
    extrato.append(transaction)

def is_valid_dposit(deposit_value : float):
    if deposit_value <= 0:
        erro_msg = "\n Operação invalida.\n O valor do depósito deve ser maior que zero."
        return False, erro_msg
    elif is_on_daily_transaction_limit():
        erro_msg = "\n Operação invalida.\n Limite de transações excedido."
        return False, erro_msg
    return True, "\n Depósito efetuado" 

def deposit(deposit_value : float):
    global saldo, extrato
    saldo += deposit_value
    deposit_date = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
    transaction={'data':deposit_date, 'tipo': "Depósito", 'valor':deposit_value}
    extrato.append(transaction)

def show_bank_statement():
    global extrato, saldo
    print("\n=============== EXTRATO ===============")
    if len(extrato) == 0:
        print("\n Não foram realizadas movimentações.")
    else:
        for transaction in extrato:
            print(f"\n {transaction['data']} {transaction['tipo']}: {transaction['valor']}")
        print(f"\n Saldo: R${saldo}")
    print("\n=======================================")


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