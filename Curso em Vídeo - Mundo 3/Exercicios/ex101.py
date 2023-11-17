from datetime import date

def voto(anoNascenca=None, anoAtual=2023):
    if anoNascenca is None:
        return "Um ano de nascença precisa ser passado como parâmetro."

    idade = anoAtual - anoNascenca

    if 16 <= idade < 18:
        return "O seu voto é opcional."
    elif idade < 16:
        return "Você não pode votar."
    else:
        return "O seu voto é obrigatório."



ano = int(input("Informe o ano de nascença: "))
print(voto(ano, date.today().year))
