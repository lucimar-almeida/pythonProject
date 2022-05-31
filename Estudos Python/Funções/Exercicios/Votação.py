def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return print(f'A idade é {idade} e não vota!')
    elif 16 <= idade < 18 or idade > 65:
        return print(f'A idade é {idade} e o voto não é obrigatorio!')
    else:
        return print(f'A idade é de {idade} e o voto é obrigatorio!')


nasc = int(input('Qual ano você nasceu? '))
print(voto(nasc))
