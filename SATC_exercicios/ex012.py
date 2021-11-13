opcao = 'S'
while opcao == 'S':
    preco = float(input('Informe o valor do carro: '))
    ano = int(input('Informe o ano do carro: '))

    if ano <= 2000:
        novopreco = (preco / 100 * -12) + preco
    elif ano > 2000:
        novopreco = (preco / 100 * -7) + preco

    print('O valor do carro a ser pado será de R$:{}{:.2f}{}'.format('\033[31m', novopreco, '\033[m'))
    print('')
    opcao = str(input('Deseja continuar cauculando os descontos? (S)sim e (N)não:')).upper().strip()
