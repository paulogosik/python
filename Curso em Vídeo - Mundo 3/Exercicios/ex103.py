def ficha(jogador="<desconhecido>", gols="0"):
    print(f"O jogador {jogador} fez {gols} gol(s) no campeonato.")


jog = input("Informe o nome do jogador: ")
gol = input("Informe a quantidade de gols marcados: ")
print("-" * 15)

if len(jog) == 0 and len(gol) == 0:
    ficha()
elif len(jog) == 0 and len(gol) != 0:
    ficha(gols=gol)
elif len(jog) != 0 and len(gol) == 0:
    ficha(jogador=jog)
else:
    ficha(jog, gol)
