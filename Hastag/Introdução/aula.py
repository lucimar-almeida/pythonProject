meta = 1000

vendas_funcionario_1 = 1000
vendas_funcionario_2 = 770
vendas_funcionario_3 = 2700


if vendas_funcionario_1 >= 1000:
    print('O funcionario 1 ganhou {} bonus.'.format(meta * 0.1))
else:
    print('O funcionario 1 não ganhou bônus.')

if vendas_funcionario_2 >= 1000:
    print('O funcionario 2 ganhou {} bonus.'.format(meta * 0.1))
else:
    print('O funcionario 2 não ganhou bônus.')

if vendas_funcionario_3 >= 1000:
    print('O funcionario 3 ganhou {} bonus.'.format(meta * 0.1))
else:
    print('O funcionario 3 não ganhou bônus.')

print('-----------------------------------------')


if vendas_funcionario_1 >= 2000:
    bonus = (vendas_funcionario_1 * 0.015)
elif vendas_funcionario_1 < 2000:
    bonus = (vendas_funcionario_1 * 0.01)
else:
   bonus = 0
print('O funcionario 1 ganhou {} de bônus!'.format(bonus))

if vendas_funcionario_2 >= 2000:
    bonus = (vendas_funcionario_2 * 0.015)
elif vendas_funcionario_2 < 2000:
    bonus = (vendas_funcionario_2 * 0.01)
else:
    bonus = 0
print('O funcionario 2 ganhou {} de bônus!'.format(bonus))

if vendas_funcionario_3 >= 2000:
    bonus = (vendas_funcionario_3 * 0.015)
elif vendas_funcionario_3 < 2000:
    bonus = (vendas_funcionario_3 * 0.01)
else:
    ponus = 0
print('O funcionario 3 ganhou {} de bônus!'.format(bonus))

print('-----------------------------------------')


meta_funcionario = 10000
meta_loja = 250000
vendas_funcionario = 5000
vendas_loja = 200000

if vendas_funcionario > meta_funcionario and vendas_loja > meta_loja:
    bonus = 0.03 * vendas_funcionario
    print('Bônus do funcionario foi de {}.'.format(bonus))
else:
    print('O funcionario não ganhou bônus.')

print('-----------------------------------------')

nota_meta = 9
nota_funcionario = 5

if nota_funcionario >= nota_meta or (vendas_funcionario > meta_funcionario and vendas_loja > meta_loja):
    bonus = vendas_funcionario * 0.015
    print('O funcionario ganhou {} de bônus!'.format(bonus))
else:
    print('O funcionario não ganhou bônus!')