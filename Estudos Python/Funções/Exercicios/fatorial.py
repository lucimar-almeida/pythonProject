def fatorial(n, show=False):
    """
    -> Calcula o fatorial de número
    :param n: O número a ser calculado
    :param show: (Opcional) mostra ou não o desenvolvimento do fatorial
    :return: O valor do fatorial de um número
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# Programa principal
num = int(input(f'Digitie um numero: '))
print(fatorial(num))

help(fatorial)