print('|================= Loja Gabriel =================|')
preco = float(input(' Informe o preço das suas compras R$: '))
print('''|================================================|
|             Formas de pagamentos               |
|                                                |
|   [1] à vista dinheiro/cheque: 10% de desconto |
|   [2] à vista no cartão: 5% de desconto        |
|   [3] em até 2x no cartão: preço normal        |
|   [4] 3x ou mais no cartão: 20% de juros       |
==================================================''')
opcao = int(input(''))
if opcao == 1:
    valorfinal = preco - (preco / 100 * 10)
elif opcao == 2:
    valorfinal = preco - (preco / 100 * 5)
elif opcao == 3:
    valorfinal = preco
elif opcao == 4:
    parcela = int(input('Em quantas parcelas? '))
    valorparcela = preco / parcela
    valorfinal = preco + (preco / 100 * 20)
    print('O valor de sua parcela foi de R$:{:.2f}'.format(valorparcela))
print('O valor de sua compra é de R$:{:.2f}'.format(valorfinal))
