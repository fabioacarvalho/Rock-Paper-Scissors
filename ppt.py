import random

ppt = ['Pedra', 'Papel', 'Tesoura']

jogo = []

def escolha():
    esc = random.choice(ppt)
    jogo.append(esc)


start = True

# MENU
def menu():
    print('')
    print('----------- JOGO PEDRA PAPEL TESOURA ----------')
    print('')
    print(' [1] - Pedra \n [2] - Tesoura \n [3] - Papel \n [4] - Sair do Jogo')
    print('')

while start == True:
    menu()

    esc = int(input('Escolha uma opção: '))
    print('')

    if esc == 1:
        pe = 'Pedra'
        jogo.append(pe)
    if esc == 2:
        te = 'Tesoura'
        jogo.append(te)
    if esc == 3:
        pa = 'Papel'
        jogo.append(pa)
    elif esc == 4:
        start = False
    
    print('Computador escolhendo...')
    print('')
    escolha()

    if jogo[0] == 'Pedra' and jogo[1] == 'Tesoura':
        print(f' Jogador: {jogo[0]} \n Computador: {jogo[1]}')
        print('Parabens você ganhou!!')
    elif jogo[0] == 'Pedra' and jogo[1] == 'Papel':
        print(f' Jogador: {jogo[0]} \n Computador: {jogo[1]}')
        print('Ish se deu mal, você perdeu :( ')
    elif jogo[0] == 'Pedra' and jogo[1] == 'Pedra':
        print(f' Jogador: {jogo[0]} \n Computador: {jogo[1]}')
        print('Empate, escolha de novo..')
        
    elif jogo[0] == 'Tesoura' and jogo[1] == 'Tesoura':
        print(f' Jogador: {jogo[0]} \n Computador: {jogo[1]}')
        print('Empate, escolha de novo..')
    elif jogo[0] == 'Tesoura' and jogo[1] == 'Papel':
        print(f' Jogador: {jogo[0]} \n Computador: {jogo[1]}')
        print('Parabens você ganhou!!')
    elif jogo[0] == 'Tesoura' and jogo[1] == 'Pedra':
        print(f' Jogador: {jogo[0]} \n Computador: {jogo[1]}')
        print('Ish se deu mal, você perdeu :( ')

    elif jogo[0] == 'Papel' and jogo[1] == 'Papel':
        print(f' Jogador: {jogo[0]} \n Computador: {jogo[1]}')
        print('Empate, escolha de novo..')
    elif jogo[0] == 'Papel' and jogo[1] == 'Pedra':
        print(f' Jogador: {jogo[0]} \n Computador: {jogo[1]}')
        print('Parabens você ganhou!!')
    elif jogo[0] == 'Papel' and jogo[1] == 'Tesoura':
        print(f' Jogador: {jogo[0]} \n Computador: {jogo[1]}')
        print('Ish se deu mal, você perdeu :( ')
    
    jogo = []
