# import random
#
# n = random.randint(1, 5)
# chose = print(input('Adivinhe o número que o computador pensou? '))
# if chose == n:
#     print('Parabens, você acertou o número que o computador pensou!')
# else:
#     print('Você perdeu, o número pensado pelo computador foi {}!'.format(n))

#--------------------------------------------------------------------------------------------------------

nome = str(input('Qual é o seu nome? '))
if nome == 'Lucimar':
    print('Que nome lindo!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é popular no Brasil!')
elif nome in 'Ana Claudia Jessica Juliana':
    print('Seu nome é feminino.')
else:
    print('Seu nome é normal')
print('Tenha um bom dia {}'.format(nome))