import random
vitoria = 0
jogadas = 0

while True:
    computador = random.randint(0, 10)
    
    print('===' * 5)
    print('Vamos jogar Par ou Impar')
    print('===' * 5)

    numero = int(input('Digite um numero de 0 a 10: '))
    NumeroTotal = numero + computador
    jogadas += 1
    escolha = ' '

    while escolha not in 'PI':
        escolha = str(input('Par ou impar? [P/I]')).strip().upper()[0]
    print(' ')
    print(f'Voce jogou {numero} e o computador jogou {computador} o total deu {NumeroTotal}')

    if escolha == 'P':
        if NumeroTotal % 2 == 0:
            print('Você venceu')
            vitoria += 1
        else:
            print('você perdeu')
            break

    elif escolha == 'I':
        if NumeroTotal % 2 == 1:
            print('você venceu')
            vitoria += 1
        else:
            print('Você perdeu')
            break
    print('Vamos jogar novamente...')
print(f'Você jogou {jogadas} vezes e venceu {vitoria}')




    

