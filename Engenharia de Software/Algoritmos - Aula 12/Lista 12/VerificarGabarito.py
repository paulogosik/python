# gabarito = ["E", "A", "B", "C", "C", "D", "E", "A", "C", "D"]
gabarito = []
respostas = []
erros = 0
i = 0

while len(gabarito) < 10:
    questaoG = input(f"=> Informe o gabarito da questão {len(gabarito) + 1}: ")
    questaoG = questaoG.upper()
    gabarito.append(questaoG)
print(f"------------------------------")
while len(respostas) < 10:
    questaoA = input(f"=> Informe a resposta da questão {len(respostas) + 1}: ")
    questaoA = questaoA.upper()
    
    if questaoA != gabarito[i]:
        erros += 1    
    respostas.append(questaoA)
    i += 1
    
print(f"------------------------------")
print(f"=> Números de questões erradas: {erros}")
if erros <= 4:
    print(f"=> Situação do aluno: APROVADO!")
else:
    print(f"=> Situação do aluno: REPROVADO!")