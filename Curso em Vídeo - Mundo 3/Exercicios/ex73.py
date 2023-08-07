teams = ('Botafogo', 'Flamengo', 'Fluminense', 'Palmeiras', 'Bragantino', 'Grêmio', 'Athletico-PR', 'Cuiabá', 'São Paulo', 'Atlético-MG',
          'Cruzeiro', 'Internacional', 'Fortaleza', 'Corinthians', 'Goiás', 'Bahia', 'Santos', 'Coritiba', 'Vasco', 'América-MG')

print(f"=> Brasileirão list of teams: {teams}")
print(f"----------------------")
print(f"=> The first 5 teams are: {teams[0:5]}")
print(f"----------------------")
print(f"=> The last 4 are: {teams[16:]}")
print(f"----------------------")
print(f"=> Teams in alphabetical order: {sorted(teams)}")
print(f"----------------------")
print(f"=> 'Cuiabá' is in the {teams.index('Cuiabá') + 1}° position.")