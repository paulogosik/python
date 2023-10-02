from ex1_calculo import *

while True:
    print("-" * 30)
    print("Escolha entre as funções:\n"
          "\t[1] Calcular a área do triângulo\n"
          "\t[2] Calcular a área do círculo\n"
          "\t[3] Calcular a área do quadrado\n"
          "\t[4] Sair")
    opc = int(input("=> "))
    print("-" * 30)

    if opc == 1:
        a = float(input("Informe o lado A: "))
        b = float(input("Informe o lado B: "))
        print(f"A área do triângulo é: {areaTriangulo(a, b)}")
    elif opc == 2:
        r = float(input("Informe o valor do raio: "))
        print(f"A área do círculo é: {areaCirculo(r)}")
    elif opc == 3:
        ld1 = float(input("Informe o lado 1: "))
        ld2 = float(input("Informe o lado 2: "))
        print(f"A área do quadrado é: {areaQuadrado(ld1, ld2)}")
    elif opc == 4:
        break
