soma = 0
for c in range(1, 7):
    numero = float(input('Informe o {}° número: '.format(c)))
    if numero % 2 == 0:
        soma = numero + soma
print('A soma dos números pares digitados é : {}'.format(soma))
