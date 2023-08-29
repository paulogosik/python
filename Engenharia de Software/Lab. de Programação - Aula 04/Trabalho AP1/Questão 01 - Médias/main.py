import funcoes
lista_nomes_notas = []

for i in range(3):
    nome = input(f"=> Informe o nome do aluno {i + 1}: ")
    lista_nomes_notas.append(nome)
    
    for c in range(2):
        nota = float(input(f"=> Informe a {c+ 1}° nota do aluno {i + 1}: "))
        lista_nomes_notas.append(nota)
    print(f"-" * 45)
    
alunos, medias = funcoes.gerar_medias(lista_nomes_notas)
i = 0
while i < len(alunos):
    print(f"=> Aluno: {alunos[i]} - Média: {medias[i]}")
    i += 1