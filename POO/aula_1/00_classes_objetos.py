class Bicicleta:

    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("SOM DE BUZINA")

    def parar(self):
        print("Parando a bicicleta... bicicleta parada")
    
    def andar(self):
        print("Pedalando")

    def get_cor(self):   #Toda classe que estancia um objeto deve ter o primeiro parametro como self.
        return self.cor
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"


b1 = Bicicleta("verde", "caloi", 2018, 1900)

b1.andar()
b1.buzinar()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta("Vermelho", "Monark", 1990, 300)
Bicicleta.buzinar(b2)
print(b2.get_cor())

print(Bicicleta.get_cor(b1))
print(Bicicleta.get_cor(b2))

print(b1)
print(b2)