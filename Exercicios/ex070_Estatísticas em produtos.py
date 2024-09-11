totalGasto = 0
produtosCaros = 0
count = 0
produtoBarato = ''

while True:
    nome = input('Qual o nome do produto: ')
    preco = float(input('Qual o preço do Produto: '))
    count += 1

    totalGasto += preco

    if preco > 1000:
        produtosCaros += 1
    
    if count == 1:
        menorPreco = preco
        produtoBarato = nome
    
    if menorPreco > preco:
        produtoBarato = nome

    opcao = ' '
    while opcao not in 'SN':
        opcao = str(input('deseja Sair? [S/N]')).strip().upper()[0]

    if opcao == 'S':
        break

print(f'O total gasto foi de {totalGasto}')
print(f'{produtosCaros} produtos custam mais de 1000 Reais ')
print(f'O produto mais barato é {produtoBarato}')



    

