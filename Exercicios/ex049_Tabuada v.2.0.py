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


numero = int(input('Informe o numero da tabuada: '))

print('====={}Tabuada{}====='.format(cor.GREEN, cor.CLEAR))
for c in range(1, 11):
    print('{}{} X {}{} = {}{}{}'.format(cor.GREEN, numero, c, cor.CLEAR, cor.RED, (numero * c), cor.CLEAR))
