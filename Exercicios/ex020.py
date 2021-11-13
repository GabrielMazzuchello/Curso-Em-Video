from random import shuffle

nome1 = input('Primeiro nome:')
nome2 = input('Segundo nome:')
nome3 = input('Terceiro nome:')
nome4 = input('Quarto nome:')

lista = [nome1, nome2, nome3, nome4]
shuffle(lista)

print("")
print('A ordem de apresentação do trabalho será:')
print(lista)
