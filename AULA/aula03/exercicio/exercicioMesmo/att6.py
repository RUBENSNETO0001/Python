# Faça um programa personalizado que dê bom dia se a hora atual for até 12 horas, boa tarde se for entre 12 horas e 18 horas e boa noite se for após as 18 horas (utilize a função DateTime).


import datetime

data_atual = datetime.datetime.now()

if data_atual.hour >= 6 and data_atual.hour < 12:
    print("Bom dia")
elif data_atual.hour >= 12 and data_atual.hour < 18:
    print("Boa tarde")
else:
    print("boa noite")