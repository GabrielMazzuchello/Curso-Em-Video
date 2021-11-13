s = float(input('qual erá o salario do funcionario? R$'))
aul = s * 15 / 100
print('o salario do funcionari que andes custava R${:.2f} agora com 15% de aumento custará R${:.2f}'.format(s, (s+aul)))
