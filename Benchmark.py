import time
from math import sqrt

def calc_1():
    for i in range(0, 100000):
        tt = i ** 2
def calc_2():
    for i in range(0, 100000):
        tt = i ** 2 // 7 * 35
def calc_3():
    for i in range(0, 100000):
        tt = sqrt(i ** 2 // 7 * 35) * 6

while True:
    q1 = int(input('Qual é o modo de benchmark quer realizar? '))

    start = time.time()

    match q1:
        case 1:
            calc_1()
        case 2:
            calc_2()
        case 3:
            calc_3()
        case _:
            print('Input inválido')
            break

    end = time.time()
    temp = end - start

    print(f'Para fazer os calculos o computador demorou: {temp} segundos')

    q2 = int(input('Quer continuar?\n1-SIM\n2-NÃO'))
    if q2 == 2:
        break
    elif q2 != 1:
        print('Input inválido')
        break

#0.005390644073486328
#0.012660741806030273
#0.027431249618530273
