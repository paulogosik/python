ministrantes = [['11C', 'mestre', 40],
['22C', 'doutor', 10],
['33C', 'mestre', 20],
['44C', 'especialista', 40],
['55C', 'especialista', 60],
['66C', 'mestre', 20],
['77C', 'especialista', 10],
['88C', 'doutor', 30]]
i = 0
mestres40Horas = 0

while i < len(ministrantes):
    print(f"Código: {ministrantes[i][0]} - Titulação: {ministrantes[i][1]} - Qt. de horas: {ministrantes[i][2]}")
    
    titulacao = ministrantes[i][1]
    horas = ministrantes[i][2]
    
    if titulacao == "especialista":
        valorRecebido = horas * 50
        ministrantes[i].append(valorRecebido)
    elif titulacao == "mestre":
        if horas < 40:
            mestres40Horas = mestres40Horas + 1
        valorRecebido = horas * 100
        ministrantes[i].append(valorRecebido)
    elif titulacao == "doutor":
        valorRecebido = horas * 150
        ministrantes[i].append(valorRecebido)
    
    i = i + 1

print("----------------------------------")
i = 0
while i < len(ministrantes):
    print(ministrantes[i])
    i = i + 1

print("----------------------------------")
print(f"=> Quantidade de ministrantes que são mestres e trabalharam menos que 40 horas: {mestres40Horas}")

print("----------------------------------")
titulacaoInformada = input("=> Informe uma titulação: ")
i = 0
while i < len(ministrantes):
    titulacao = ministrantes[i][1]
    
    if titulacao == titulacaoInformada:
        print(f"Código: {ministrantes[i][0]} - Valor recebido: {ministrantes[i][3]}")
    
    i = i + 1