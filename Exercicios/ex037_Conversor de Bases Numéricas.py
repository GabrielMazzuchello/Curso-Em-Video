numero = int(input('informe um numero Inteiro: '))
print('')
print('''|=======================================|
|      Escolha para converter           |
|      1° converter para Binario        |
|      2° Converter para OCTAL          |
|      3° Converter para HEXADECIMAL    |
|=======================================|''')
opcao = int(input('Sua opção: '))

print('')
if opcao == 1:
    print('{} convertido para Binario corresponde há {}{}{}'.format(numero, '\033[31m', bin(numero)[2:], '\033[m'))

elif opcao == 2:
    print('{} convertido para Octal corresponde há {}{}{}'.format(numero,  '\033[31m', oct(numero)[2:], '\033[m'))

elif opcao == 3:
    print('{} convertido para HEXADECIMAL corresponde há {}{}{}'.format(numero, '\033[31m', hex(numero)[2:], '\033[m'))

else:
    print('{}       Opção invalida       {}'.format('\033[34m', '\033[m'))
