frase = str(input('Digite uma frase ')).strip()

print('Aparece {} vezes a letra A'.format(frase.upper().count('A')))
print('A primeira letra A apareseu na posição {}'.format(frase.find('A')+1))
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1))
