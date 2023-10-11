meta = 50000
qtde_vendida = 60000

if qtde_vendida > meta:
    print(f'Batemos a meta de unidades vendidas, vendemos {qtde_vendida}!')
else:
    print(f'Não batemos a meta, a quantidade vendida foi de {qtde_vendida} !')

print('-----------------------------------------')

email = input('Insira seu email: ')

if not '@' in email and '.com' in email:
    print('Email invalido!')
else:
    print('Email valido!')

meta = 1000

vendas_funcionario_1 = 1000
vendas_funcionario_2 = 770
vendas_funcionario_3 = 2700

