alf = {
    'A': 'o-', 'B': '-ooo', 'C': '-o-o', 'D': '-oo', 'E': 'o', 'F': 'oo-o',
    'G': '--o', 'H': 'oooo', 'I': 'oo', 'J': 'o---', 'K': '-o-', 'L': 'o-oo',
    'M': '--', 'N': '-o', 'O': '---', 'P': 'o--o', 'Q': '--o-', 'R': 'o-o',
    'S': 'ooo', 'T': '-', 'U': 'oo-', 'V': 'ooo-', 'W': 'o--', 'X': '-oo-',
    'Y': '-o--', 'Z': '--oo', ' ': '/'}

q1 = input('Insira o que quer traduzir para código morse: ')
q1 = q1.upper()

list = []

for i in q1:
    list.append(alf[i])

for i in list:
    print(i, end=' ')