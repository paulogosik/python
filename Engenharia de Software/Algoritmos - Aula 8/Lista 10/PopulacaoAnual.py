ano = int(input("=> Informe o ano atual: "))
populacao = int(input("=> Informe a população total atual: "))

while ano < 2050:
    print(f"=> {ano} - {populacao:.2f}")
    
    populacaoPorcentagem = populacao * 0.1
    populacao += populacaoPorcentagem
        
    ano += 1