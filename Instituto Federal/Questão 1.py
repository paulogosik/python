distancia = int(input('Dois carros (X e Y) partem em uma mesma direção. O carro X sai com velocidade constante de 60 Km/h e o carro Y sai com velocidade constante de 90 Km/h.\n'
                      'Em uma hora (60 minutos) o carro Y consegue se distanciar 30 quilômetros do carro X, ou seja, consegue se afastar um quilômetro a cada 2 minutos.\n'
                      'Diga a distância e direi o tempo que levou:'))
tempo = distancia * 2
print('Levou {} minutos!'.format(tempo))
