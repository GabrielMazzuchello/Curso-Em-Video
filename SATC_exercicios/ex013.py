vetcustos = []
vetprecos = []

for i in range(3):
    vetcustos.append(float(input('Informe o custo de um produto: ')))
    vetprecos.append(float(input('Informe o preço da vendo do produto: ')))

    if vetcustos[i] == vetprecos[i]:
        print('Não houve lucro e nem prejuiso')
    elif vetcustos[i] < vetprecos[i]:
        print('Houve lucro')
    else:
        print('houve prejuizo')

print('custo: {}'.format(vetcustos))
print('venda: {}'.format(vetprecos))

