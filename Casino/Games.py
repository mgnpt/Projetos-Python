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
    cor = ''
    evorod = ''
    One_To_Eighteen = False    #1 até 18
    Nineteen_To_ThirtySix = False    #19 até 36
    Fr_Twelve = False    #Primeiros 12 números
    Sc_Twelve = False    #12 números no meio
    Th_Twelve = False    #Últimos 12 números
    Fr_Two_To_One = False    #1º 2to1
    Sc_Two_To_One = False    #2º 2to1
    Th_Two_To_One = False    #3º 2to1
    if n1 == 0:
        resultado = '0'
        cor = 'Green'
        evorod = 'Nenhum'
    elif 1 <= n1 <= 10 or 19 <= n1 <= 28:
        if n1 % 2 == 0:
            resultado = f'{n1}'
            cor = 'Preto'
            evorod = 'Par'
        else:
            resultado = f'{n1}'
            cor = 'Vermelho'
            evorod = 'Impar'
    else:  # 11 até 18 e 29 até 36
        if n1 % 2 == 0:
            resultado = f'{n1}'
            cor = 'Vermelho'
            evorod = 'Par'
        else:
            resultado = f'{n1}'
            cor = 'Preto'
            evorod = 'Impar'
    if 1 <= n1 <= 18:     #Verificar se n1 está na 1ª parte ou 2ª
        One_To_Eighteen = True
    elif 19 <= n1 <= 36:
        Nineteen_To_ThirtySix = True

    if 1 <= n1 <= 12:     #Verificar em que grupo de 12 números n1 está
        Fr_Twelve = True
    elif 13 <= n1 <= 24:
        Sc_Twelve = True
    elif 25 <= n1 <= 36:
       Th_Twelve = True

    if n1 % 3 == 0:    #Verificar em que 2to1 grupo n1 está
        Th_Two_To_One = True
    elif (n1-1) % 3 == 0:
        Sc_Two_To_One = True
    else:
        Fr_Two_To_One = True

    print(f'{resultado} - {cor} - {evorod}')
