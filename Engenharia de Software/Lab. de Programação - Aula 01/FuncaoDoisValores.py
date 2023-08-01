def par_ou_impar(valor):
    if valor % 2 == 0:
        print(f"=> O valor '{valor}' é par")
    else:
        print(f"=> O valor '{valor}' é ímpar") 
           
num = int(input(f"=> Informe um valor inteiro: "))
par_ou_impar(num)