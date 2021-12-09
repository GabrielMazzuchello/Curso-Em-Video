from datetime import date
nascimento = []

for c in range(7):
    nascimento.append(int(input('Informe o ano que nasceu há {}° pessoa: '.format(c+1))))

for c in range(len(nascimento)):
    anoatual = date.today().year
    idade = anoatual - nascimento[c]

    if idade >= 18:
        print('\nVocê é MAIOR de idade! --> Sua idade {}'.format(idade))
    else:
        print('\nVocê é MENOR de idade! --> Sua idade {}'.format(idade))
