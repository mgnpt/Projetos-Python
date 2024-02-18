alf = {
    'A': 'o-', 'B': '-ooo', 'C': '-o-o', 'D': '-oo', 'E': 'o', 'F': 'oo-o',
    'G': '--o', 'H': 'oooo', 'I': 'oo', 'J': 'o---', 'K': '-o-', 'L': 'o-oo',
    'M': '--', 'N': '-o', 'O': '---', 'P': 'o--o', 'Q': '--o-', 'R': 'o-o',
    'S': 'ooo', 'T': '-', 'U': 'oo-', 'V': 'ooo-', 'W': 'o--', 'X': '-oo-',
    'Y': '-o--', 'Z': '--oo', ' ': '/',
    '1': 'o----', '2': 'oo---', '3': 'ooo--', '4': 'oooo-', '5': 'ooooo',
    '6': '-oooo', '7': '--ooo', '8': '---oo', '9': '----o', '0': '-----',
    '.': 'o-oo-oo', ',': '--oo--', '?': 'oo--oo', '!': '-o--o-','(': '-oo-o', ')': '-oo-o-',
    ':': '---ooo', ';': '-o-oo-', '"': 'o-o-oo'
        }

q1 = input('Insira o que quer traduzir para código morse: ')
q1 = q1.upper()

mrs_cd = []

for i in q1:
    mrs_cd.append(alf[i])

for i in mrs_cd:
    print(i, end=' ')
