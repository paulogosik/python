print('=> Qual é a sua profissão?\n'
      '  "Estudante"\n'
      '  "Professor"\n'
      '  "Profissional"')
profissao = input('=> ')
profissao = profissao.capitalize()
cursos = input('=> Deseja participar dos mini-cursos? "S" para Sim ou "N" para Não. ')
cursos = cursos.upper()
traducao = input('=> Precisa de tradução simultânea? "S" para Sim ou "N" para Não. ')
traducao = traducao.upper()
print('--------------------')

if profissao == 'Estudante' or profissao == 'Professor':
    if cursos == 'S' and traducao == 'S':
        print(f'=> Profissão: {profissao}\n=> Valor da inscrição: R$170.00')
    elif cursos == 'S' and traducao == 'N':
        print(f'=> Profissão: {profissao}\n=> Valor da inscrição: R$150.00')
    elif cursos == 'N' and traducao == 'S':
        print(f'=> Profissão: {profissao}\n=> Valor da inscrição: R$120.00')
    else:
        print(f'=> Profissão: {profissao}\n=> Valor da inscrição: R$100.00')
elif profissao == 'Profissional':
    if cursos == 'S' and traducao == 'S':
        print(f'=> Profissão: {profissao}\n=> Valor da inscrição: R$220.00')
    elif cursos == 'S' and traducao == 'N':
        print(f'=> Profissão: {profissao}\n=> Valor da inscrição: R$200.00')
    elif cursos == 'N' and traducao == 'S':
        print(f'=> Profissão: {profissao}\n=> Valor da inscrição: R$170.00')
    else:
        print(f'=> Profissão: {profissao}\n=> Valor da inscrição: R$150.00')
else:
    print('=> Opção indisponível!')