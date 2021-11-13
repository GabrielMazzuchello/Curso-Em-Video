from random import randint
numeroescolhido = randint(0, 5)
escolha = int(input('Adivinhe o numero que o computador escolheu entre 0 e 5: '))
if numeroescolhido == escolha:
    print('parabens você acertou')
else:
    print('Que pena você errou, Boa Sorte na proxima ')
    print('O numero era {}'.format(numeroescolhido))
