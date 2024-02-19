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
    print(n1)
    rest = n1 // 2
    if n1 == 0:
        resultado = '0 - Green'
        print(resultado)
    if rest == 0:
        resultado = f'{n1} - Preto'
        print(resultado)
    else:
        resultado = f'{n1} - Vermelho'
        print(resultado)

roulette()
