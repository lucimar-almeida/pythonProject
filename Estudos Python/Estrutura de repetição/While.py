# for c in range(1, 10):
#     print(c)
# print('Fim')
#
# c = 1
# while c < 10:
#     print(c)
#     c = c + 1
# print('Fim!')

#--------------------------------------------------------------
#
# n = 1
# while n != 0:
#     n = int(input('Digite um número: '))
# print('Fim!')

#-------------------------------------------------------------------

# r = 'S'
# while r == 'S':
#     n = int(input('Digite um número: '))
#     r = str(input('Quer continuar [S/N]? ')).upper()
# print('Fim!')

#---------------------------------------------------------------

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if  n % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
print('Você digitou {} números pares e {} números ímpares!'.format(par, impar))
