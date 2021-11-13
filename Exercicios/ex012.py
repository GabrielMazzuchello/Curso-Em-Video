v = float(input('qual e o valor do seu produto? R$:'))
d = v / 100 * 5
print('o valor do produto de R$:{} agora com 5% de desconto ficou R$:{:.2f}'.format(v, (v-d)))
