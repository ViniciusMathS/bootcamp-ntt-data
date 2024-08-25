conta_normal = True
conta_universitaria = False

saldo = 2000
saque = 500
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado.")
    elif saque <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial.")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado.")
    else:
        print("Saldo insuficiente.")    