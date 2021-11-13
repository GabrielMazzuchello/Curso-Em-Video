# Desenvolva uma calculadora que possua um menu, tratamento de erro caso o usuario escolha uma operação invalida e utilize funções na mesma
def calculadora(numero1, numero2, operacao):
    if operacao == '+':
        print(numero1 + numero2)
    elif operacao == '-':
        print(numero1 - numero2)
    elif operacao == '*':
        print(numero1 * numero2)
    elif operacao == '/':
        print(numero1 / numero2)
    else:
        print('Operação invalida Reinicie o programa!!')


print('========================================')
print('|      Informe o primeiro numero       |')
print('|      Informe a operação + - * /      |')
print('|      Informe o segundo numero        |')
print('========================================')
numero1 = float(input(''))
operacao = str(input(''))
numero2 = float(input(''))

print('Resultado...')
print(calculadora(numero1, numero2, operacao))
