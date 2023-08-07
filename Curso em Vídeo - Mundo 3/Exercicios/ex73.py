tabela = ('Botafogo', 'Flamengo', 'Fluminense', 'Palmeiras', 'Bragantino', 'Grêmio', 'Athletico-PR', 'Cuiabá', 'São Paulo', 'Atlético-MG',
          'Cruzeiro', 'Internacional', 'Fortaleza', 'Corinthians', 'Goiás', 'Bahia', 'Santos', 'Coritiba', 'Vasco', 'América-MG')

print(f"=> Lista de time do Brasileirão: {tabela}")
print(f"----------------------")
print(f"=> Os 5 primeiros são: {tabela[0:5]}")
print(f"----------------------")
print(f"=> Os últimos 4 são: {tabela[16:]}")
print(f"----------------------")
print(f"=> Times em ordem alfabética: {sorted(tabela)}")
print(f"----------------------")
print(f"=> O Cuiabá está na {tabela.index('Cuiabá') + 1}ª posição.")