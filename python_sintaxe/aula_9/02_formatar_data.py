from datetime import datetime

data_hora_atual = datetime.now()

data_hora_str = "2024-11-15 15:35" 

mascara_ptbr = "%A - %d/%m/%Y %H:%M"
mascara_en ="%Y-%m-%d %H:%M"

print(data_hora_atual.strftime(mascara_ptbr)) # converte de datetime para str

print(datetime.strptime(data_hora_str, mascara_en)) # converte de str para datetime