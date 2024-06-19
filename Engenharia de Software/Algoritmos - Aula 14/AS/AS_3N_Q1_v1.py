qtVoltas = 0
tempoCorrida = 0
tempo = int(input("Tempo da volta: "))
while tempo != 0:
        posi = int(input("Posição do carro na volta:"))
        qtVoltas = qtVoltas + 1
        tempoCorrida = tempoCorrida + tempo
        tempo = int(input("Tempo da volta: "))
print("Quantidade de voltas:", qtVoltas)
print("Tempo de demorou:", tempoCorrida)
print("A posição do carro ao final da corrida:", posi)
