from random import randint
from Games import *

perfis = []
perfil_atual = None

CoinFlip = False  # Quando escolher o valor fica True
Roulette = False  # Quando escolher o valor fica True
Blackjack = False  # Quando escolher o valor fica True

cont = False

def menu(a):
    print("-" * 20)
    print(f"WELCOME {a}")
    print("-" * 20)

def def_perfil():
    q2 = input('Qual é o nome do perfil? ')
    q2 = q2.capitalize()
    perfis.append(q2)
    print(perfis)

def sel_perfil():
    if not perfis:
        def_perfil()
    else:
        q2 = int(input(f'Qual é o seu perfil?\n1-{perfis[0]}\n2-{perfis[1]}'))

def sel_game(a):
    global CoinFlip, Roulette, Blackjack
    q4 = int(input(f'Olá {a}, qual é o jogo que quer jogar?\n1-Cara ou Coroa\n2-Roullete\n3-Blackjack'))
    if q4 == 1:
        CoinFlip = True
    elif q4 == 2:
        Roulette = True
    elif q4 == 3:
        Blackjack = True

def cont_jogo():
    q4 = int(input('Quer continuar a jogar?\n1-SIM\n2-NÃO'))
    if q4 == 2:
        return False
    elif q4 == 1:
        return True

while True:
    if not perfis:
        perfil_atual = perfis[0] if perfis else 'Jogador'
    menu(perfil_atual)

    q2 = int(input('Quer jogar ou trocar de perfil?\n1-JOGAR\n2-TROCAR DE PERFIL\n3-SAIR\nEscolha: '))

    if q2 == 3:
        print(f'Obrigado por jogar {perfil_atual}')
        break
    elif q2 == 2:
        sel_perfil()
        continue
    elif q2 == 1:
        while True:
            sel_game(perfil_atual)
            if CoinFlip:
                coin_flip()
                if not cont_jogo():
                    break
            elif Roulette:
                roulette()
                if not cont_jogo():
                    break
            elif Blackjack:
                blackjack()
                if not cont_jogo():
                    break
