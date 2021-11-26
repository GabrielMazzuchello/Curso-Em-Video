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


numero = int(input('Digite um numero: '))
tot = 0
for c in range(1, numero + 1):
    if numero % c == 0:
        tot += 1
        print(cor.GREEN, end='')
    else:
        print(cor.RED, end='')

    print('{} {}'.format(c, cor.CLEAR), end='')

print('\n\nO numero {} foi dividido {} vezes!'.format(numero, tot))

if tot == 2:
    print('Por tanto ele é {}PRIMO{}'.format(cor.BLUE, cor.CLEAR))
else:
    print('Por tanto ele {}NÂO É PRIMO!{}'.format(cor.RED, cor.CLEAR))
