sexo = str(input('Me diga seu sexo:'))
if sexo == "masculino":
    alt = float(input('Me diga sua altura:'))
    pesoi = alt*72.7-58
    print('O seu peso devia ser {}!'.format(pesoi))
else:
    alt = float(input('Me diga sua altura:'))
    pesoi = alt * 62.1 - 44.7
    print(pesoi)