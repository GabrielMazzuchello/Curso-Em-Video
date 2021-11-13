num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
num3 = int(input('Terceiro valor: '))

# Verificação do menor numero
menor = num3
if num2 < num3 and num2 < num1:
    menor = num2
if num1 < num3 and num1 < num2:
    menor = num1

# verificação do maior numero
maior = num3
if num2 > num1 and num2 > num3:
    maior = num2
if num1 > num2 and num1 > num3:
    maior = num1
print('O menor numero é {}'.format(menor))
print('O maior numero é {}'.format(maior))
