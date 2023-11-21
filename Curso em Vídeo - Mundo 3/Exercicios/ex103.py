def ficha(jogador="<desconhecido>", gols="0"):
    print(f"O jogador {jogador} fez {gols} gol(s) no campeonato.")


jogador = input("Informe o nome do jogador: ")
gols = input("Informe a quantidade de gols marcados: ")
print("-" * 15)

if len(jogador) == 0 and len(gols) == 0:
    ficha()
elif len(jogador) == 0 and len(gols) != 0:
    ficha(gols=gols)
elif len(jogador) != 0 and len(gols) == 0:
    ficha(jogador=jogador)
else:
    ficha(jogador, gols)
