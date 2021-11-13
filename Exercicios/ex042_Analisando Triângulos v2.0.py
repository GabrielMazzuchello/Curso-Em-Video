def analisedotriangulo():

    if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
        print('As Tres retas {}PODEM FORMAR{} um triângulo!'.format('\033[34m', '\033[m'))
        print('')
        if r1 != r2 != r3 != r1:
            print('O triângulo é {}ESCALENO{}, possui todos os lados com medidas diferentes!'.format('\033[35m',
                                                                                                     '\033[m'))
        elif r1 == r2 == r3:
            print('O triângulo é {}EQUILÁTERO{}, possui todos os lados iguais!'.format('\033[34m', '\033[m'))

        else:  # <-- o mesmo que r1 == r2 != r3 or r1 == r3 != r2 or r2 == r3 != r3:
            print('O triângulo é {}ISÓCELES{}, possui dois dos lados iguais e um diferente!'.format('\033[36m', '\033[m'))

    else:
        print('As tres retas {}NÂO PODEM FORMAR{} um triângulo!'.format('\033[31m', '\033[m'))


print('========================')
print('  Analisando Triângulo')
print('========================')

r1 = float(input('primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
print('')
analisedotriangulo()
