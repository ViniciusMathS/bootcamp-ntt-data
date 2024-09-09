import requests
import json

def get_something(cep : str) -> dict:
    request = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
    print("get something: ")
    print("status code response: ", request.status_code)
    #print("content response: ", request.content)
    all_fields = json.loads(request.content)
    return all_fields

def get_all() -> list:
    request = requests.get(f"http://127.0.0.1:5000/carros")
    print("get all: ")
    print("status code response: ", request.status_code)
    #print("content response: ", request.content)
    all_fields = json.loads(request.content)
    return all_fields

class Endereco:
    def __init__(self, cep, logradouro, complemento, unidade, bairro, localidade, uf, estado, regiao, ibge, gia, ddd, siafi):
        self.cep = cep
        self.logradouro = logradouro
        self.complemento = complemento
        self.unidade = unidade
        self.bairro = bairro
        self.localidade = localidade
        self.uf = uf
        self.estado = estado
        self.regiao = regiao
        self.ibge = ibge
        self.gia = gia
        self.ddd = ddd
        self.siafi = siafi

endereco = Endereco(**get_something("88138154"))

print(f"{endereco.logradouro}, 485, {endereco.bairro}, {endereco.localidade} - {endereco.uf}")

