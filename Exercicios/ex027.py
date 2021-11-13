nome = str(input('Digite seu nome completo :')).strip()
nome1 = nome.split()

print('prazer em conheser(lo)!!')
print('Seu primeiro nome é {}'.format(nome1[0]))
print('Seu ultimo nome é {}'.format(nome1[len(nome1)-1]))
