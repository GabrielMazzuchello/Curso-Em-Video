num = count = soma = 0
num = int(input('Digite um numero [999 para parar]'))

while num != 999:
    soma += num
    count += 1
    num = int(input('Digite um número [999 para parar]'))
print('Vorê digitou {} números e a soma entre eles foi {}.'.format(count, soma))