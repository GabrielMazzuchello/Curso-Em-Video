import random


class cor:
    BLACK = '\033[30m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    GRAY = '\33[37m'
    WHITE = '\033[97m'
    CLEAR = '\033[m'


computador = random.randint(1, 10)
print('Acabei de pensar em um numero de 1 ate 10!')
print('Quer tentar descobrir qual é?')
acertou = False
tentativa = 0

while not acertou:
    palpite = int(input('Qual é o seu palpite? '))
    tentativa += 1

    if palpite == computador:
        acertou = True
        print('{}Parabens você acestou!, em {} tentativas{}'.format(cor.CYAN, tentativa, cor.CLEAR))

    elif computador < palpite < 11:
        print('{}Humm, quase e MENOS!!{}'.format(cor.RED, cor.CLEAR))

    elif computador > palpite > -1:
        print('{}Humm, quase e MAIOR!!{}'.format(cor.RED, cor.CLEAR))

    elif palpite > 10:
        print('{}OPS lembre-se os numeros são entre 0 e 10{}'.format(cor.YELLOW, cor.CLEAR))
