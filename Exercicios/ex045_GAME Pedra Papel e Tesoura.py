import random

itens = ('Pedra', 'Papel', 'Tesoura')  # lista de itens
computador = random.randint(0, 2)  # o computador esta sorteando entre 0, 1 ou 2

print(''' Suas opções 
 [1] Pedra
 [2] Papel
 [3] Tesoura''')
player = int(input('Qual é sua jogada? \n'))

print('=--=' * 7)
print('O computador jogou: {}{}{}'.format('\033[34m', itens[computador], '\033[m'))
print('O jogador jogou: {}{}{}'.format('\033[31m', itens[player], '\033[m'))
print('=--=' * 7)

print()
if computador == 0:  # computador jogou PEDRA
    if player == 0:
        print('O jogo enpatou!')
    elif player == 1:
        print('Jogador vence!')
    elif player == 2:
        print('Computador vence!')
    else:
        print('Jogada invalida!!!')

elif computador == 1:  # computador jogou PAPEL
    if player == 1:
        print('o jogo enpatou!')
    elif player == 0:
        print('Computador vence!')
    elif player == 2:
        print('Jogador vence!')
    else:
        print('Jogada invalida!!!')

elif computador == 2:  # computador jogou TESOURA
    if player == 2:
        print('O jogo enpatou!')
    elif player == 1:
        print('Computador vence!')
    elif player == 0:
        print('Jogador vence')
    else:
        print('Jogada invalida!!!')
