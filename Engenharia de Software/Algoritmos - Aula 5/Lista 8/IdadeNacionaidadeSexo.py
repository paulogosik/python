i = 0
homensBR = 0
idosos = 0
idadeTotal = 0

while i < 6:
    i += 1
    idade = int(input("=> Qual é a idade? "))
    nacionalidade = input("=> Qual é a nacionalidade? ")
    sexo = input("=> Qual é o sexo? Digite 'M' para masculino ou 'F' para feminino. ")
    print('----------------------------------')

    sexo = sexo.upper()
    nacionalidade = nacionalidade.lower()
    idadeTotal = idadeTotal + idade

    if sexo == "M" and nacionalidade == 'brasileiro' and idade >= 20 and idade <= 30:
        homensBR = homensBR + 1
    elif idade >= 65 and (nacionalidade == 'brasileiro' or nacionalidade == 'italiano' or nacionalidade == 'frances'):
        idosos = idosos + 1

media = idadeTotal / 6

print(f"=> Quantidade de homens brasileiros entre 20 e 30 anos: {homensBR}")
print(f"=> Quantidade de idosos braileiros, italianos ou franceses: {idosos}")
print(f"=> Média de idades: {media:.2f}")