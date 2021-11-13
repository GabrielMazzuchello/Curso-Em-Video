print('========================')
print('  Analisando Triângulo')
print('========================')

r1 = float(input('primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))
print('')

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As Tres retas {}PODEM FORMAR{} um triângulo'.format('\033[34m', '\033[m'))
else:
    print('As tres retas {}NÂO PODEM FORMAR{} um triângulo'.format('\033[31m', '\033[m'))
