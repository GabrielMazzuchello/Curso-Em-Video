totalGasto = 0
produtosCaros = 0
precoBarato = 99999999999
produtoBarato = ''

while True:
    nome = input('Qual o nome do produto: ')
    preco = float(input('Qual o preço do Produto: '))

    totalGasto += preco

    if preco > 1000:
        produtosCaros += 1
    
    if preco < precoBarato:
        precoBarato = preco
        produtoBarato = nome

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('deseja Sair? [S/N]')).strip().upper()[0]

    if opcao == 'S':
        break

print(f'O total gasto foi de {totalGasto}')
print(f'{produtosCaros} produtos custam mais de 1000 Reais ')
print(f'O produto mais barato é {produtoBarato}')



    

