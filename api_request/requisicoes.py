import requests
import json

def get_something():
    request = requests.get("https://viacep.com.br/ws/88138154/json/")
    print("get something: ")
    print("status code response: ", request.status_code)
    #print("content response: ", request.content)
    all_fields = json.loads(request.content)
    return all_fields

class Endereco:
    def __init__(self, cep, logradouro, complemento, unidade, bairro, localidade, uf, ibge, gia, ddd, siafi):
        self.cep = cep
        self.logradouro = logradouro
        self.complemento = complemento
        self.unidade = unidade
        self.bairro = bairro
        self.localidade = localidade
        self.uf = uf
        self.ibge = ibge
        self.gia = gia
        self.ddd = ddd
        self.siafi = siafi

endereco = Endereco(**get_something())

print(endereco.cep, endereco.uf, endereco.logradouro)

