cores = {'vermelho': '\033[31m',
         'limpa': '\033[m',
         'verde': '\033[34m'}

preco = float(input('informe o valor do seu produto:'))
parcela = int(input('Informe em quantas vezes quer parcelar:'))
print('')
vetparcela = []

for i in range(parcela):
    vetparcela.append(preco / parcela)

print('O valor de seu produto R$:{} parcelado em {} Vezes de R$:{}{:.2f}{} por parcela'.format(preco, parcela, cores['vermelho'], (preco/parcela), cores['limpa']))
print('')
for i in range(parcela):
    print('A parcela N° {}{}{} De valor {}{:.2f}{}'.format(cores['verde'], i + 1, cores['limpa'], cores['vermelho'], vetparcela[i], cores['limpa']))
