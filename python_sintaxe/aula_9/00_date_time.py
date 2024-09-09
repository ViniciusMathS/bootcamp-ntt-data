from datetime import date, datetime, time

data = date(2023, 8, 14) # retorna um objeto no formato date # YYYY-MM-DD
print(data) 

print(date.today()) # retorn data atual # YYYY-MM-DD

print(datetime.now()) # retorna data e hora atual # YYYY-MM-DD hh:mm:ss.microsegundos

print(datetime.today())

data_hora = datetime(2023, 8, 14, 7, 58, 34) # parametros: Ano, Mês, Dia, Hora, Minuto, Segundos 
print(data_hora)

hora = time(18, 40, 0) 
print(hora)
