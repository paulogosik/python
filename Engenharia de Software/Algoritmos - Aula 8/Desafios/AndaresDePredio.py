andar = 0
pessoas = 0
andares = int(input("=> Qual o número de andares do prédio? "))
print("-------------------------")

while andar < andares:
    andar += 1
    
    print(f"=> {andar}° andar!")
    entrada = int(input("=> Quantas pessoas iram entrar no elevador? "))
    saida = int(input("=> Quantas pessoas iram sair do elevador? "))
    
    pessoas += entrada
    pessoas -= saida
    
    if pessoas > 15:
        print(f"=> Excesso de passageiros, {pessoas - 15} devem sair")
        pessoas = 15
    
    while andar != andares:
        print(f"=> {pessoas} pessoas estão subindo para o próximo.")
        break
    
    print("-------------------------")

print(f"=> {pessoas} pessoas vão descer.")