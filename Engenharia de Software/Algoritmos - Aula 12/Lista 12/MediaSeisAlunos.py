mediaAlunos = []
nomeAlunos = []
melhoresAlunos = []
i = 0
totalMedias = 0

while len(nomeAlunos) < 6:
    nome = input(f"=> Informe o nome do aluno {len(nomeAlunos) + 1}: ")
    media = float(input(f"=> Informe a média do aluno {len(nomeAlunos) + 1}: "))
    
    totalMedias += media
    nomeAlunos.append(nome)
    mediaAlunos.append(media)

mediaGeral = totalMedias / len(mediaAlunos)

while i < 6:
    if mediaAlunos[i] > mediaGeral:
        melhoresAlunos.append(nomeAlunos[i])
    i += 1

print("------------------------")
print(f"=> Média geral dos alunos: {mediaGeral}")
print(f"=> Alunos com média maior que a média geral: {melhoresAlunos}")