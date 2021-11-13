salario = float(input('Informe o valor do seu salario: '))
if salario <= 1250:
    salarioaumento = salario * 15 / 100 + salario
else:
    salarioaumento = salario * 10 / 100 + salario
print('O salário de R$:{:.2f} com o aumento passou a ser de R$:{:.2f}'.format(salario, salarioaumento))
