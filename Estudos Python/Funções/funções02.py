def contador(i, f, p):
    """
    Faz uma contagem e mostra na tela
    parametro i inicio da contagem
    parametro f fim a contagem
    parametro p passo da contagem
    """
    c = i
    while c <= f:
        print(f'{c}', end='..')
        c += p
    print('Fim!')

contador(0, 100, 2)
help(contador)

print('------------------------------------------------------------------------------------')

#Parametro opcionais

def somar(a=0, b=0, c=0):
    s = a + b + c
    print(f'A soma vale {s}.')

somar(4)

print('------------------------------------------------------------------------------------')

#Escopo de variaveis

# Uma variavel criada dentro de uma função ela tem apenas o escopo local
# logo uma variavel criada fora de uma função ela tem um escopo global, até mesmo dentro de funções.
# pode ter a mesma variavel com valores diferentes desde que tenham sido declarada em escopo diferente
# uma em escopo global e a outra em escopo local.

def função():
    n1 = 4
    print(f'N1 dentro vale {n1}')

n1 = 2
função()
print(f'N1 fora vale {n1}')

print('------------------------------------------------------------------------------------')

