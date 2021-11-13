nome = str(input('Informe o seu nome: '))
salario = float(input('Informe seu salário fixo: '))
vendas = float(input('informe o total de vendas: '))

newsalario = salario + (salario * 15 / 100)

print('Olá, {} seu salário fixo é R$:{:.2f} e o seu salário final desse mes é R$:{:.2f}'.format(nome, salario, newsalario))
