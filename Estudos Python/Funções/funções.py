def mensagem(msg):
    print('-' * 30)
    print(msg)
    print('-' * 30)


mensagem('        Curso em Vídeo')


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B é igual a {s}')


# Programa principal
soma(4, 5)


mensagem('     Empacotar parámetros')

def contador(*num):
    # for valor in num:  # Usando for para fazer uma varedura nas tuplas criadas pelo empacotador de parámetros
    #     print(f'{valor} ', end=' ')
    # print('Fim!')
    tam = len(num)
    print(f'Recebi os valores {num} e são ao todo {tam} números')


# Programa Principal
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)

mensagem('      Listas em funções')

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1


# Programa Principal
valores = [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)

mensagem('      Listas em funções')

def adição(*valores):
    s = 0
    for num in valores:
        s += num
        print(f'Somando os valores {valores} temos {s}')


adição(5, 2)
adição(2, 9, 4)