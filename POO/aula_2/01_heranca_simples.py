class Veiculo:

    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print(f"Ligando o motor da {self.__class__.__name__}.")

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

class Carro(Veiculo):
    pass

class Motocicleta(Veiculo):
    pass

class Caminhao(Veiculo):

    def __init__(self, cor, placa, numero_rodas, carregado=False): # Sobreescrevendo o inicializador
        super().__init__(cor, placa, numero_rodas)
        self.carregado = carregado

    def is_carregado(self):
        print(f"{'Sim' if self.carregado else 'Não'} está carregado")





moto = Motocicleta("Preto", "xyz-0987", 2)
moto.ligar_motor()

carro = Carro("Branco", "pki-8300", 4)
carro.ligar_motor()

caminhao = Caminhao("Vermelho", "scn-2004", 8, True)
caminhao.ligar_motor()
caminhao.is_carregado()

print(caminhao)
print(moto)
print(carro)