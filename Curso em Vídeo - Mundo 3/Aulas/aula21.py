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


print(contador.__doc__)
