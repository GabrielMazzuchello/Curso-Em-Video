n1 = int(input('Digite um numero:'))
cores = {'amarelo': '\033[33m',
         'limpa': '\033[m',
         'vermelha': '\033[31m'}
print('analisando o valor {}{}{} o seu antecesor é {}{}{} e seu sucessor é {}{}{}'.format(cores['amarelo'], n1, cores['limpa'],
                                                                                          cores['vermelha'], (n1-1), cores['limpa'],
                                                                                          cores['vermelha'], (n1+1), cores['limpa']))
