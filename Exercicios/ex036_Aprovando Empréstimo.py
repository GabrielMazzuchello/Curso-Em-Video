casa = float(input('Informe o valor da casa: R$'))
salario = float(input('Informe o seu salario: R$'))
parcela = int(input('Informe em quantos Anos irá financiar: '))

minimo = casa / (parcela * 12)

print('')
print('A casa de R$:{:.2f} parcelada em {} anos, Cada prestação será de R$:{:.2f}'.format(casa, parcela, minimo))
if minimo >= 30 * (salario / 100):
    print('O enprestimo foi {}negado{}!'.format('\033[31m', '\033[m'))
else:
    print('O enprestimo foi {}aprovado{}!'.format('\033[34m', '\033[m'))
