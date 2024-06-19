import random, string
letras = []
i=0
while i < 10:
    letras.append(random.choice(string.ascii_letters).upper()) 
    i=i+1        
print(letras)

vogais = ['A', 'E', 'I', 'O', 'U']

qtVogais = 0
i=0

while i<10:
        if letras[i] in vogais: #todas vez que tiver uma vogal ele retorna verdaeiro
                print("Posição:", i, "Possui a vogal:", letras[i])
                qtVogais = qtVogais + 1
        i = i + 1
if qtVogais == 0:
        print("Não tem vogais na lista!")

