import funcao  # type: ignore

cpf = input(f"=> Informe seu CPF (siga o exemplo 111.222.333-44): ")
somaTotal = funcao.somar_cpf(cpf)

print(f"=> A soma do número [{cpf}] é: {somaTotal}")
