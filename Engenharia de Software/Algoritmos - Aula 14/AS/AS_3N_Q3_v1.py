aulasJaneiro = [['João', 'iniciante', 60],
['Maria', 'intermediário', 90],
['Pedro', 'avançado', 75],
['Ana', 'iniciante', 60],
['Lucas', 'avançado', 90],
['Julia', 'iniciante', 60],
['Mariana', 'avançado', 75],
['Gustavo', 'intermediário', 60]]

totalHorasAvancado = 0

print(aulasJaneiro)

print("\nAcrescenta valor-------------------------------------")
i = 0
while i < len(aulasJaneiro):
                if aulasJaneiro[i][1] == 'iniciante':
                        aulasJaneiro[i].append(aulasJaneiro[i][2]*8)
                elif aulasJaneiro[i][1] == 'intermediário':
                        aulasJaneiro[i].append(aulasJaneiro[i][2]*10)
                else:
                        aulasJaneiro[i].append(aulasJaneiro[i][2]*12)

                print(aulasJaneiro[i])
                i = i + 1
                
print("\nDiminui iniciante------------------------------------")
i = 0
while i < len(aulasJaneiro):
        if aulasJaneiro[i][1] == 'iniciante':
                aulasJaneiro[i][2]  = aulasJaneiro[i][2]  - 5
                aulasJaneiro[i][3] = aulasJaneiro[i][2] * 8 #recalcula valor
        elif aulasJaneiro[i][1] == 'avançado':
                totalHorasAvancado =  totalHorasAvancado  + aulasJaneiro[i][2] 
        print(aulasJaneiro[i])
        i = i + 1

print("\nTotal de horas de aulas para avançado:", totalHorasAvancado)

posi = int(input("Digite a posição que quer imprimir: "))
print("O nome que está na posição escolhida é:", aulasJaneiro[posi][0])

#Não tem na prova, mas, se eu quisesse pesquisar a posição de um nome
nome = input("Digite o nome: ")
i = 0
while i < len(aulasJaneiro):
        if aulasJaneiro[i][0] == nome:
                print(nome, "está na posição", i)
        i = i + 1

