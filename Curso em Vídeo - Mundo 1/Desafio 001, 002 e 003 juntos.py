print('====== Sempre pressione "Enter" para continuar ;) ======')

nome = input('Olá, qual é o seu nome?')

print('Olá ' + nome + '!' + ' Prazer em te conhecer!' + ' Eu sou James, o assistente pessoal do Paulo!')

resposta = input('Tudo bem eu te fazer algumas perguntas?')

print('====== Responda com números ======')

dia = input('Em qual dia você nasceu?')

mês = input('Em qual mês você nasceu?')

ano = input('Em qual ano você nasceu?')

print('Você nasceu no dia' , dia + ' do' , mês + ' de' , ano)

respostaa = input('Correto?')

print('Agora, um pequeno jogo de matemática.')

pn = int(input('Coloque um número de qualquer tamanho:'))

sn = int(input('Coloque mais um:'))

rf = pn + sn

print('A soma entre {} e {} é igual a {}'.format(pn, sn, rf))


