
# a=5+3*2
# print('a:', a)

# b=5**2
# print('b:', b)

# c=19//2
# print('c:', c)

# d=365*522
# print('d:', d)

# e=18%2
# print('e:', e)

# f=122%3
# print('f:', f)

# g=4**3
# print('g:', g)

# h=pow(4,3)
# print('h:', h)

# i=81**(1/2)
# print('i:', i)

# j=25**(1/2)
# print('j:', j)

# l=127**(1/3)
# print('l:', l)

# #---------------------------------------------------

# print('oi'*5)

#-----------------------------------------------------

#nome = input('Qual é o seu nome?')
#print('Prazer em te conhecer {:^=20}!'.format(nome))

#----------------------------------------------------

# n1 = int(input('Um valor: '))
# n2 = int(input('Outro valor: '))
# s = n1 + n2
# m = n1 * n2
# d = n1 / n2
# di = n1 // n2
# e = n1 ** n2
# print('A soma vale: {}, a multiplicação vale: {}, a divisão vale: {:.3f}'.format(s, m, d), end=' ')
# print('O resto vale: {} \n a exponenciação vale: {}.'.format(di, e))

#-------------------------------------------------

#Exercicio 01 -> Faça um programa que leia um número e mostre na tela  o seu sucessor e seu antecessor

# n = int(input('Digite um número: '))
# ant = n - 1
# suc = n +1
# print('O número digitado é {}\n Seu antecessor é {}\n Seu sucessor é {}'.format(n, ant, suc))

#----------------------------------------------------

# Exercicio 02 -> Crie um algoritmo que leia um número e mostre o seu dobro, triplo, e raiz quadrada.
#
# n = int(input('Digite um número: '))
# dobro = 2*n
# triplo = 3*n
# raiz = n**(1/2)
# print('O número digitado foi: {}\nO dobro é: {}\nO triplo é: {}\nRaiz quadrada: {:.0f}'.format(n, dobro, triplo, raiz))
#
# ---------------------------------------------------------
#
# Exercicio 03 -> Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua medía.
#
# nome = input("Aluno: ")
# n1 = int(input('Digite a nota 1: '))
# n2 = int(input('Digite a nota 2: '))
# media = (n1+n2)/2
# print('O aluno(a) {} tem notas:\nNota 1: {}\nNota 2: {}\nMédia de: {}'.format(nome, n1, n2, media))
#
# -------------------------------------------------------
#
# Exercicio 04 -> Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
#
# valor = int(input('Digite um valor em metros(m): '))
# cent = valor*100
# mili = valor*1000
# print('{} metros são equivalentes a: {} centimentros e a {} milimetros.'.format(valor, cent, mili))
#
# ------------------------------------------------------
#
# Exercicio 05 -> Faça um programa que leia um número inteiro qualquer e mostre a sua tabuada
#
#
# n = int(input('Digite um número: '))
# a = 1*n
# b = 2*n
# c = 3*n
# d = 4*n
# e = 5*n
# f = 6*n
# g = 7*n
# h = 8*n
# i = 9*n
# j = 10*n
# print('Tabuada do {0}\n1x{0} = {1}\n2x{0} = {2}\n3x{0} = {3}\n4x{0} = {4}\n5x{0} = {5}\n6x{0} = {6}\n7x{0} = {7}\n8x{0} = {8}\n9x{0} = {9}\n10x{0} = {10}'.format(n, a, b, c, d, e, f, g, h, i, j))

#-----------------------------------------------

#Exercicios 6 -> Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar

# saldo = int(input('Qual o saldo da sua conta: '))
# dolar = int(input('Qual valor do cambio hoje: '))
# comprar = (saldo/dolar)
# print(comprar)
# print('Com o saldo da sua conta você pode comprar {} dolares.'.format(comprar))


#-----------------------------------------------

#Exercicico 7 -> Faça um programa que leia a largura e a altura de uma parede em metros, clacule a sua área e a quantidade de tinta necessaria para pinta-la, sabendo que cada litro de tinta, pinta uma área de 2m2

# sal = int(input('Digite o salario: '))
# porc = int(input('digite quanto foi o aumento em porcentagem: '))
# aumento = ((sal*porc)/100)+sal
# print('O salario recebeu um acrescimo de {} porcento e agora é de {} Reais.'.format(porc, aumento))

# #---------------------------------------------

#Exercicio 8 -> Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

# precop = int(input('Qual o valor do produto: '))
# desconto = int(input('Qual é a porcentagem do desconto: '))
# newprice = (precop -((precop*desconto)/100))
# print('O novo valor do produto é de {} reais'.format(newprice))