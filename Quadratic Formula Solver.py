from math import sqrt

def quadratic_formula(a, b, c):
    tt_mais = (-b +sqrt(b**2 - 4 * a * c)) / (2 * a)
    tt_menos = (-b -sqrt(b**2 - 4 * a * c)) / (2 * a)
    print(f'X é igual a {tt_mais:.2f} ou a {tt_menos:.2f}')


n1 = float(input('Qual é o primeiro número? '))
n2 = float(input('Qual é o segundo número? '))
n3 = float(input('Qual é o terceiro número? '))

quadratic_formula(n1, n2, n3)
