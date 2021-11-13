n1 = int(input('digite um numero:'))
n2 = int(input('digite outro:'))
s = n1 + n2

cores = {'limpa': '\033[m',
         'vermelho': '\033[0;31m',
         'amarelo': '\033[0;33m'}
print('a soma entre {}{}{} e {}{}{} corresponde {}{}'.format(cores['amarelo'], n1, cores['limpa'], cores['amarelo'], n2,
                                                             cores['limpa'], cores['vermelho'], s, cores['limpa']))
