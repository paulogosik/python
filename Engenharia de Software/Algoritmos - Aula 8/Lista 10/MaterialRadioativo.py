contSegundos = 0
massa = float(input("=> Informe a massa em gramas: "))

while massa > 0.5:
    contSegundos += 50
    massa = massa / 2

horas = contSegundos // 3600
fMin = contSegundos % 3600
minutos = fMin // 60
segundos = fMin % 60
print(f"=> {horas} horas, {minutos} minutos e {segundos} segundos.")