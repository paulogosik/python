# Ver a documentações de funções!!!
    # help(input)
    #
    # for i in range(3):
    #     print("=" * 30)
    #
    # print(input.__doc__)
    #
    # for i in range(3):
    #     print("=" * 30)

def contador(i, f, p):
    """
    => Função criada para printar uma contagem customizada, podendo customizar o início, o fim e os passos.
    :param i: Indica o início, qual será o número inicial.
    :param f: Indica o final, qual será o número final.
    :param p: Indica os passos da função, de quantos em quantos números irá haver a contagem.
    :return: Esta função não retorna nada, apenas printa os números do contador.
    @Created by Paulo Moita | https://github.com/paulogosik
    """
    for cont in range(i, f+1, p):
        print(cont, end=' ')
    print(f"\nFim!")


def linha(c='-', t=30):

    """
    => É uma função que retorna o print de uma linha com o tamanho informado e o caracter informado.
    :param c: É informado o caracter que será usado para fazer a linha, o caracter '-' está como padrão.
    :param t: É informado o tamanho da linha, o tamanho 30 está como padrão.
    :return: Esta função não retorna nada, apenas printa a linha customizada.
    @Created by Paulo Moita | https://github.com/paulogosik
    """

    print(f"{c}" * t)


def somarTresNumeros(a=0, b=0, c=0):
    soma = a + b + c
    print(f"O resultado da soma é: {soma}")


print(contador.__doc__)
linha('*', 120)
print(linha.__doc__)
linha()
somarTresNumeros(3, 2, 5)
linha(t=15)
somarTresNumeros()
linha()
