arq = open("C:/Users/paulomoita/Documents/python/Engenharia de Software/Lab. de Programação - Aula 13/notas.txt", "r")

for line in arq.readlines():
    print(line.strip("\n"))
