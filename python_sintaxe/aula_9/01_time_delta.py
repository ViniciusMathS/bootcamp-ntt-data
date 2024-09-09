from datetime import datetime, timedelta, date, time

CAR_TYPES = {
    'P' : 30,
    'M' : 45,
    'G' : 60
}

data_atual = datetime.now()

for tipo_carro, tempo in CAR_TYPES.items():

    data_estimada = data_atual + timedelta(minutes=tempo)
    print(f"\nUm carro de porte {tipo_carro} fiacra pronto às {data_estimada}")

print(date.today() - timedelta(days=1))

print((datetime(2014, 4, 21, 10, 19, 20) - timedelta(hours=1)).time())