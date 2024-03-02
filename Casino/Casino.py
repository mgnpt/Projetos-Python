from Games import *

perfis = []
perfil_atual = None

CoinFlip = False  # Quando escolher o valor fica True
Roulette = False  # Quando escolher o valor fica True
Blackjack = False  # Quando escolher o valor fica True

cont = False
vt = 0     #nº de vitórias
dnh = 100    #dinheiro do jogador
ttl_jgs = 0    #total de jogos

def menu(a):
    print("-" * 20)
    print(f"WELCOME {a}")
    print("-" * 20)

def def_perfil():
    q2 = input('Qual é o nome do perfil? ')
    q2 = q2.capitalize()
    perfis.append({'name': q2, 'money': 100, 'wins': 0, 'total_games': 0})
    print(perfis)

def sel_perfil():
    if not perfis:
        def_perfil()
    else:
        q2 = int(input(f'Qual é o seu perfil?\n1-{perfis[0]["name"]}\n2-{perfis[1]["name"]}'))

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

def calc_perc_vt(vt, ttl_jgs):
    if ttl_jgs == 0:
        return 0
    return (vt / ttl_jgs) * 100

def save_stats(nm_jg, dnh, vt, ttl_jgs):
    with open('stats_jgr.txt', 'a') as file:
        perc_vt = calc_perc_vt(vt, ttl_jgs)
        file.write(f"Nome: {nm_jg}\nDinheiro: {dnh}\n% de vitórias: {perc_vt:.2f}%\n")

while True:
    if not perfis:
        perfil_atual = 'Jogador'
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
            # Depois de cada jogo atualizar as estatísticas do jogador.
            for jogador in perfis:
                save_stats(jogador['name'], jogador['money'], jogador['wins'], jogador['total_games'])
