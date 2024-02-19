#from random import randint

perfis = []
perfil_atual = None
def menu(a):
    print("-" * 20)
    print(f"WELCOME {a}")
    print("-" * 20)

def def_perfil():
    q2 = input('Qual é o nome do perfil? ')
    q2 = q2.capitalize()
    perfis.append(q2)


while True:
    q1 = int(input('Quer continuar?\n1-SIM\n2-NÃO\n3-TROCAR DE PERFIL'))

    if q1 == 2:
        break
    elif q1 == 3:
        q3 = int(input('Quer usar um perfil já existente ou criar um?\n1-Perfil existente\n2-Perfil novo'))

        if q3 == 2:
            perfil_atual = def_perfil()

        elif q3 != 1:
            print(perfis)
            perfil_atual = input("Escolha o perfil existente: ")
        else:
            print('Input inválido')

        menu(perfil_atual)

    elif q1 == 1:
        if perfil_atual != None:  # Check if a profile is selected
            menu(perfil_atual)
        else:
            print("Nenhum perfil selecionado.")


    elif q1 != 1:
        print('Input inválido')
        break