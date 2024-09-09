class Cachorro:
    
    def __init__(self, nome, cor, acordado=True): # método construtor ou inicializador.
        self.nome=nome
        self.cor=cor
        self.acordado=acordado

    def latir(self):
        print("Cachorro latindo")

    def __del__(self): # Destrói a instacia do objeto, liberando espaço em memória.
        print("Removendo a instância da classe.")

def criar_cachorro():
    c = Cachorro("Zeus", "Branco", False)
    print(c.nome)

c = Cachorro("Rex", "Caramelo")
c.latir()

print("Olá Mundo.")
print("Olá Mundo.")

del c # Força a destruição do objeto antes do fim do programa.

print("Olá Mundo.")
print("Olá Mundo.")
print("Olá Mundo.")

criar_cachorro()