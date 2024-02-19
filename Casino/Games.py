from random import randint

def coin_flip():
    n1 = randint(1, 2)
    if n1 == 1:
        resultado = 'Cara'
        print(resultado)
    elif n1 == 2:
        resultado = 'coroa'
        print(resultado)


def par(a):
    a % 2 == 0
def impar(a):
    a % 2 != 0

def roulette():
    n1 = randint(0, 36)
    print(n1)
    cor = ''
    evorod = ''
    if n1 == 0:
        resultado = '0 - Green'
        cor = 'Green'
    elif 1 <= n1 <= 10 or 19 <= n1 <= 28:
        if n1 % 2 == 0:
            resultado = f'{n1} - Preto'
            cor = 'Preto'
            evorod = 'Par'
        else:
            resultado = f'{n1} - Vermelho'
            cor = 'Vermelho'
            evorod = 'Impar'
    else:  # 11 até 18 e 29 até 36
        if n1 % 2 == 0:
            resultado = f'{n1} - Vermelho'
            cor = 'Vermelho'
            evorod = 'Par'
        else:
            resultado = f'{n1} - Preto'
            cor = 'Preto'
            evorod = 'Impar'
    print(resultado)
    print(evorod)
#Falta adicionar se é par ou impar, 3 * 2 to 1 e 1 to 18 e 19 to 36
roulette()
