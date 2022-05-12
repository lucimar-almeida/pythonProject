# num = [2, 5, 9, 1]
#
# num[2] = 3
#
# num.append(7) #adiciona o elemento na ultima posição
#
# num.sort() #ordena a lsita
#
# #num.sort(reverse=True) #ordena de forma decrescente
#
# num.insert(2, 0) #insere o 0 na posição [2]
#
# num.pop() #elimina a ultima posição (index), mas pode colocar nos parenteses o index que deseja excluir
#
# num.remove(2) #remove o elemento da lista
#
# num.append(4)
#
# if 4 in num:
#     num.remove(4)
#     print('O número 4 foi removido! ')
# else:
#     print('Não foi encontrado o número 4 na lista!')
#
# print(num)
#
# print(f'Essa lista tem {len(num)} elementos!')

#---------------------------------------------------------------------------------------------------------------------

valores = []
valores.append(5)
valores.append(9)
valores.append(4)
#print(valores)

# for v in valores:
#     print(f'{v}...', end='') #end= faz que o resultado fique na mesma linha


# for c, v in enumerate(valores): # O enumerate pega tanto a chave quanto o valor
#     print(f'Na posição {c} encontra-se o número {v}!')
# print('Cheguei no final da lista!!!')

# newValue = list() # Com essa forma da para inserir valores na lista atraves do teclado
# for cont in range(0, 5):
#     newValue.append(int(input('Digite um número: ')))
# for c, v in enumerate(newValue):
#     print(f'Na posição {c} foi encontrado {v} elemento!')
# print('Cheguei no final da lista!!!')

#---------------------------------------------------------------------------------------------------------------------

a = [2, 3, 4, 7]
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')