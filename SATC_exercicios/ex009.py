vetnuminpar = []
vetnumpar = []

intervalo = int(input('Informe o numero do intervalo: '))

for numero in range(intervalo):
    if numero % 2 == 0:
        vetnumpar.append(numero)
    else:
        vetnuminpar.append(numero)

print('-=-'*45)
print('do intervalo os numeros pares são: {}'.format(vetnumpar))
print('')
print('do intervalo os numeros inpares são: {}'.format(vetnuminpar))
print('-=-'*45)