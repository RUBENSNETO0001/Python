import datetime

data_atual = datetime.datetime.now()

if data_atual.hour >= 6 and data_atual.hour < 12:
    print("Bom dia")
elif data_atual.hour >= 12 and data_atual.hour < 18:
    print("Boa tarde")
else:
    print("boa noite")