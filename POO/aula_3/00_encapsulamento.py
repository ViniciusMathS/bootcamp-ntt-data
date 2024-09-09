class Conta:

    def __init__(self, numero_agencia, saldo=0) -> None:
        self._saldo = saldo # convenção para atributos privados ( _atributo ).
        self.numero_agencia = numero_agencia

    def sacar(self, valor):
        # ---
        self._saldo -= valor

    def depositar(self, valor):
        # ---
        self._saldo += valor

    def get_saldo(self):
        return self._saldo

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
    


account_01 = Conta('0001', 1121.50)

# O interpretador não impede o acesso, modificadores de acesso são apenas uma convenção em python.
print(account_01._saldo) 

# Forma encapsulada
print(account_01.get_saldo()) 



