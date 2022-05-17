# Projeto ADS - "Urna Eletronica"

def tela(titulo):
    print('-' * 30)
    print(titulo)
    print('-' * 30)


def space():
    print(' ')


def subtitulo(text):
    print('-' * 5, text, '-' * 5)


# Candidatos a prefeito
prefeitos = [{'Candidato': 'Ademir da Guia', 'votos': 0}, # 'Número': 10
             {'Candidato': 'João Gois', 'votos': 0}] # 'Número': 20

# Condidatos a vereadores
vereadores = [{'vereador': 'Ana Maria', 'votos': 0}, #'Número': 35401
              {'vereador': 'Luiz Herminio', 'votos': 0}, # Número': 25600
              {'vereador': 'Fernanda Silva', 'votos': 0}, # Número': 10123
              {'vereador': 'Felipe Camargo', 'votos': 0}, # Número': 10456
              {'vereador': 'Evandro Alves', 'votos': 0}, # Número': 20256
              {'vereador': 'Rafael Sugesmundo', 'votos': 0}, # Número': 20789
              {'vereador': 'Marcos Pacheco', 'votos': 0}, # Número': 10333
              {'vereador': 'Fabio Henrique', 'votos': 0}, # Número': 20963
              {'vereador': 'Jean Gomes', 'votos': 0}, # Número': 10100
              {'vereador': 'Jessica Mendes', 'votos': 0} # 'Número': 35555
              ]


#Votos brancos e nulos
nulos_brancos = [{'Nulos': 0}, {'Brancos': 0}]



tela('         Eleições 2022')

def tela_principal():
    opt = int(input('Digite "1" para Zeressima ou digite "2" para iniciar a votação: '))
    if opt != 2 != 1:
        tela_principal()
    if opt == 1:
        tela('       Zeressima')
        space()
        subtitulo('Candidatos a prefeitos')
        for e in prefeitos:
            for k, v in e.items():
                print(f'{k} {v}')
        space()
        subtitulo('Candidatos a vereador')
        for e in vereadores:
            for k, v in e.items():
                print(f'{k} {v}')
        tela_principal()

    elif opt == 2:
        tela_votação_prefeito()
def tela_votação_prefeito():
    tela('       Votação')
    space()
    subtitulo('Voto para prefeito')
    voto = int(input('Digite o número do seu candidato a prefeito'
                     '\nou digite 1 para votar em "Branco": '))
    if voto == 10:
        prefeitos[0]['votos'] += 1
        print(prefeitos)
    elif voto == 20:
        prefeitos[1]['votos'] += 1
    elif voto == 1:
        option = str(input('tem certeza que deseja votar em "BRANCO"? Sim = [S], Não = [N]: '))
        if option == 's':
            print('Seu voto foi "Branco" para prefeito.')
            nulos_brancos[1]['Brancos'] += 1
        else:
            tela_votação_prefeito()
    elif voto != 1 != 10 != 20:
        option = str(input('Tem certeza que quer anular seu voto? Sim = [S], Não = [N]: '))
        if option == 'n':
            tela_votação_prefeito()
        else:
            print('Seu voto para prefeito foi anulado.')
            nulos_brancos[0]['Nulos'] += 1
    print(prefeitos)
    print(nulos_brancos)










    # if voto = 10, 20:
    #     print('Ok')









tela_principal()





















# print(prefeitos[0]['votos'])
# print(vereadores[8]['Número'])
