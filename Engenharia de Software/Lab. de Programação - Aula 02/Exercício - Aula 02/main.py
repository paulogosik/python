from funcaoEx01 import *
from funcaoEx02 import *
from funcaoDoisValores import *
from funcaoIdade import *
from funcaoNumerosCrescentes import *
from funcaoSegundosEmHoras import *
from funcaoTresNotas import *

opc = ""
while opc != "sair":
    print(f"=> Selecione sua opção:\n"
          "     [1] Exercício 01\n"
          "     [2] Exercício 02\n"
          "     [3] Exercício Dois Valores\n"
          "     [4] Exercício Idade\n"
          "     [5] Exercício Numeros Crescentes\n"
          "     [6] Exercício Segundos em Horas\n"
          "     [7] Exercício Tres Notas\n"
          "     [Sair] Sair")
    opc = input("=> ").lower()
    
    print("-------------------")
    if opc == "1": # OPÇÃO 01 --------------------------------------------------------------------
        # Exercício 01
        verif = VerificaPositivo1(0)
        print(verif)
        
    elif opc == "2": # OPÇÃO 02 --------------------------------------------------------------------
        # Exercício 02
        verif = VerificaPositivo2(-4)
        print(f"O valor N é {verif}")
        
    elif opc == "3":# OPÇÃO 03 --------------------------------------------------------------------
        num = int(input(f"=> Informe um valor inteiro: "))
        par_ou_impar(num)
        
    elif opc == "4": # OPÇÃO 04 --------------------------------------------------------------------
        anos = int(input(f"=> Informe quantos anos você tem: "))
        meses = int(input(f"=> Tirando os anos, quantos meses: "))
        dias = int(input("=> Tirando os meses, quantos dias: "))

        idadeDias = IdadeEmDias(anos, meses, dias)
        print(f"=> Você tem {idadeDias} dias de idade")
    
    elif opc == "5": # OPÇÃO 05 --------------------------------------------------------------------
        n1 = int(input("=> Informe um número inteiro: "))
        n2 = int(input("=> Informe outro número inteiro: "))
        n3 = int(input("=> Informe mais um número inteiro: "))

        ordem = OrdemCrescente(n1, n2, n3)

        print(f"=> A ordem crescente é: {ordem}")
        
    elif opc == "6": # OPÇÃO 06 --------------------------------------------------------------------
        segundos = int(input(f"=> Informe o tempo representado em segundos: "))
        tempo = segundos_em_horas(segundos)
        
    elif opc == "7": # OPÇÃO 07 --------------------------------------------------------------------
        tipo = input("=> Informe o tipo da matéria: ").upper()
        n1 = float(input(f"=> Informe a N1: "))
        n2 = float(input(f"=> Informe a N2: "))
        n3 = float(input(f"=> Informe a N3: "))

        media = CalcularMedia(n1, n2, n3, tipo)

        print(f"=> A média do aluno foi: {media}")
    
    print("-------------------")