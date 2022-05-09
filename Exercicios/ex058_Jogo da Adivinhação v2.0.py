import random

computador = random.randint(1, 10)
print('Acabei de pensar em um numero de 1 ate 10!')
print('Quer tentar descobrir qual é?')
acertou = False
tentativa = 0

while not acertou:
    palpite = int(input('Qual é o seu palpite? '))
    tentativa += 1

    if palpite == computador:
        palpite = True
        print('Parabens você acestou!, em {} tentativas'.format(tentativa))
    elif palpite > computador:
        print('Humm quase e MENOS!!')
    elif palpite < computador:
        print('Humm quase e MAIOR!!')

