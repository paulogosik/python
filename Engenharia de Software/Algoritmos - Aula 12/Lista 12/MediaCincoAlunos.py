medias = []
contMedias = 0
mediasGerais = 0
i = 1

while i <= 5:
    media = float(input(f"=> Média do aluno {i}: "))
    medias.append(media)
    mediasGerais += media
    i += 1

mediaTotal = mediasGerais / 5

i = 0
while i < 5:
    if medias[i] > mediaTotal:
        contMedias += 1
    i += 1

print("----------------------------")
print(f"=> Média geral da turma: {mediasGerais}")
print(f"=> Quantidade de alunos com média maior que a média geral da turma: {contMedias}")