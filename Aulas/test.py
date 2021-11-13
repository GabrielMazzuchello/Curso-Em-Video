import math


def raiz():
    try:
        numero1 = float(input('Informe o numero para descobrir sua raiz: '))
        resultado = math.sqrt(numero1)
        return resultado
    except ValueError:
        print('Somente numeros')


def porcentagem():
    try:
        numero1 = float(input('Informe a porcentagem: '))
        numero2 = float(input('Informe o numero que deseja saber a porcentagem: '))
        resultado = (numero2 / 100) * numero1
        return resultado
    except ValueError:
        print('Somente numeros')


def adicao():
    resultado = numero1 + numero2
    return resultado


def subtracao():
    resultado = numero1 - numero2
    return resultado


def multiplicacao():
    resultado = numero1 * numero2
    return resultado


def divisao():
    resultado = numero1 / numero2
    return resultado


def potenciacao():
    resultado = math.pow(numero1, numero2)
    return resultado


operacao = str(input('Informe a operação "+ - * / **  raiz ou %": ')).strip()
if operacao == 'raiz':
    print('{:.2f}'.format(raiz()))
elif operacao == '%':
    print(porcentagem())
else:
    if (operacao == '+') or (operacao == '-') or (operacao == '*') or (operacao == '/') or (operacao == '**'):
        try:
            numero1 = float(input('Informe o 1° numero: '))
            numero2 = float(input('Informe o 2° numero: '))

            if operacao == '+':
                print(adicao())
            elif operacao == '-':
                print(subtracao())
            elif operacao == '*':
                print(multiplicacao())
            elif operacao == '/':
                print(divisao())
            elif operacao == '**':
                print(potenciacao())
        except ValueError:
            print('Somente numeros')
    else:
        print('Operação invalida')
