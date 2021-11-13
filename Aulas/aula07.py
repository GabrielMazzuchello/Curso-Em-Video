n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
po = n1 ** n2
print('A soma de {} e {} é de {} a multiplicação é {} e a divisão {:.3f}'.format(n1, n2, s, m, d), end=' ')
print('A divisão inteira vale {} e a potenciação é {}'.format(di, po))
