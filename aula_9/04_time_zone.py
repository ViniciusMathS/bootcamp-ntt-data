import pytz 
from datetime import datetime, date, time

mascara_ptbr = "%A - %d/%m/%Y %H:%M"
TIME_ZONES = ["Europe/Oslo", "America/Sao_Paulo", "Asia/Tokyo", "America/New_York", "Europe/London", "America/Vancouver", "Asia/Macau"]

for time_zone in TIME_ZONES:
    data_atual = datetime.now(pytz.timezone(time_zone))
    print(f" {time_zone}: {data_atual.strftime(mascara_ptbr)}\n")
