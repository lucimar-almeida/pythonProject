from uteis import números

num = int(input('Digite um número: '))

fat = números.fatorial(num)

print(f'O fatorial de {num} é {fat}.')

print(f'O dobro de {num} é {números.dobro(num)}.')

print(f'O triplo de {num} e {números.triplo(num)}.')