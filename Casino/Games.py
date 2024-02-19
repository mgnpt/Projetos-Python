from random import randint

def coin_flip():
    n1 = randint(1, 2)
    if n1 == 1:
        resultado = 'Cara'
        print(resultado)
    elif n1 == 2:
        resultado = 'coroa'
        print(resultado)

def roulette():
    n1 = randint(0, 36)
    if n1 == 0:
        resultado = '0 - Green'
    elif 1 <= n1 <= 10 or 19 <= n1 <= 28:
        if n1 % 2 == 0:  # even
            resultado = f'{n1} - Preto'
        else:
            resultado = f'{n1} - Vermelho'
    else:  # 11 to 18 and 29 to 36
        if n1 % 2 == 0:  # even
            resultado = f'{n1} - Vermelho'
        else:
            resultado = f'{n1} - Preto'
    print(resultado)

roulette()
