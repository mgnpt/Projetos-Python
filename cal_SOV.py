# Octal to Decimal Conversion
n = input("Digite um número em octal: ")  
x = 0
decimal = 0

for i in n[::-1]:
    res = int(i) * (16 ** x)  
    x += 1
    decimal += res
    print(f'{i} = {res}')
    
print(f'{n} em decimal = {decimal}')
