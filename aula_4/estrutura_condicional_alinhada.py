conta_normal = True
conta_universitaria = True
conta_especial = True

saldo = 2000
saque = 2400
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado.")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial.")
    else:
        print("Saldo insuficiente.")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado.")
    else:
        print("Saldo insuficiente.")
elif conta_especial:
    print("Conta especial selecionada.")
else:
    print("Tipo de conta invalida.")