def notas(*n, sit=False):
    """
    -> Sistema para calcular e analisar varias notas.
    :param n: variavel para receber as nota ou varias notas
    :param sit: variavel que recebe se quer saber a situação das notas do aluno
    :return: retorna as notas classificando-as e a media das mesma
    """
    r = dict()
    r['total'] = len(n)
    r['maior'] = max(n)
    r['menor'] = min(n)
    r['media'] = sum(n) / len(n)
    if sit:
        if r['media'] >= 7:
            r['Situação'] = 'Boa'
        elif r['media'] >= 5:
            r['Situação'] = 'Razoavel'
        else:
            r['Situação'] = 'Ruim'

    return r


# Programa Principal
resp = notas(1.5, 2.5, 9, 1.5, sit=True)
print(resp)
help(notas)