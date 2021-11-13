custo = float(input('Custo do produto: '))
porcento = float(input('Informe o porcento a ser adicionado ao valor: '))

total = custo / 100 * porcento + custo

print('')
print('O pruduto que custou R$:{} com o acrecimo de {}%. Valor de venda R$:{}{:.2f}'.format(custo, porcento, '\033[31m', total))
