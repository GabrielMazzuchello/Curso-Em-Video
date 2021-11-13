numero = int(input('Digite um numero: '))

u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print('Analisando o numero: {}'.format(numero))
print('Unidade(s): {}'.format(u))
print('Desena(s): {}'.format(d))
print('Centena(s): {}'.format(c))
print('Milhar(es): {}'.format(m))
