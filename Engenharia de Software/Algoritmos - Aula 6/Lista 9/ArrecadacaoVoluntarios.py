i = 0
contI = 0
contM = 0
quantM = 0
quantI = 0
meiaIdade = 0
contIdade = 0

while i < 10:
    i += 1

    idade = int(input("=> Informe a idade: "))
    carteirinha = input("=> Possui carteirinha de desconto? 'S' para sim ou 'N' para não. ")
    carteirinha = carteirinha.upper()

    if idade >= 16:
        if carteirinha == "S":
            print("=> Pode entrar! Valor pago no ingresso: R$25.00")
            print("----------------------------")
            contM += 1
            quantM += 25
            contIdade += 1
            meiaIdade += idade
        elif carteirinha == "N":
            print("=> Pode entrar! Valor pago no ingresso: R$50.00")
            print("----------------------------")
            quantI += 50
            contI += 1
        else:
            print("=> Informação de carteirinha inválida!")
            print("----------------------------")
    elif idade < 16:
        print("=> Não pode entrar!")
        print("----------------------------")

valorTotal = quantM + quantI
mediaMeia = meiaIdade / contIdade

print(f"=> Valor total arrecadado: R${valorTotal}")
print(f"=> Média de idade das pessoas que pagaram meia: {mediaMeia}")

if contM > contI:
    print(f"=> Mais participantes pagaram meia que inteira.")
elif contM < contI:
    print(f"=> Mais participantes pagaram inteira que meia.")
else:
    print("=> O número das pessoas que pagaram meia ou inteira é o mesmo.")