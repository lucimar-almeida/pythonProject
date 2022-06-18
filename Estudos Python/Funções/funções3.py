# def contador(i, f, p):
#     """
#     -> Faz uma contagem e mostra na tela
#     :param i: Inicio da contagem
#     :param f: fim da contagem
#     :param p: passo da contagem
#     :return: sem retorno
#     Fução criada por: Lucimar Almeida da Silva
#     """
#     c=i
#     while c<=f:
#         print(c, end='..')
#         c+=p
#     print("Fim!")
# contador(2, 10, 2)
# help(contador)
#
#
# contador(2, 10, 2)
# help(contador)
#
# def somar(a=0, b=0, c=0):
#     s = a + b + c
#     print(f'A soma é {s}')
#
# somar(10, 100)


def adicao(a=0, b=0, c=0):
    s = a + b + c
    return s

r1 = adicao(10, 84, 100)
r2 = adicao(84, 100)
r3 = adicao(10, 84,)

print(f'Os resultados obtidos foram {r1}, {r2}, {r3}.')

def fatorial(num=1):
    f=1
    for c in range(num, 0, -1):
        f*=c
    return f
n = int(input('Digite um número: '))
print(f'O fatorial de {n} é {fatorial(n)}.')