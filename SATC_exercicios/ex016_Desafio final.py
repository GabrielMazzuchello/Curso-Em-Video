import math
# criar uma cauculadora que possua [+] Adição [-] Subtração[*] Multiplicação [/] Divizão [**] Potenciação
# [raiz] Raiz Quadrada [%] Porcentagem. E que só pare de funcionar se o usuario pedir use a biblioteca math (se quiser)
# teste do github


def raiz():
    try:  # tratamento de erro e resultado separado
        numero1 = float(input('Informe o numero para descobrir sua raiz: '))
        resultado = math.sqrt(numero1)
        return resultado
    except ValueError:
        print('Somente numeros')


def porcentagem():
    try:  # tratamento de erro e resultado separado
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


while True:
    print(f'''    |{' Operação ':=^30}|
    |       [+] Adição             |
    |       [-] Subtração          |
    |       [*] Multiplicação      |
    |       [/] Divizão            |
    |       [**] Potenciação       |
    |       [raiz] Raiz Quadrada   |
    |       [%] Porcentagem        |
    |       [S] Sair               |
    |{'=' * 30}|''')
    operacao = str(input()).strip()

    if operacao == 'raiz':
        print('{:.1f}'.format(raiz()))

    elif operacao == '%':
        print(porcentagem())

    elif operacao.upper() == 'S':
        print('{: ^30}'.format('Fim do Programa'))
        break

    else:  # verificado a operação
        if (operacao == '+') or (operacao == '-') or (operacao == '*') or (operacao == '/') or (operacao == '**'):
            try:  # tratamento de erro
                numero1 = float(input('Informe o 1° numero: '))
                numero2 = float(input('Informe o 2° numero: '))

                if operacao == '+':  # chamando as funçoes
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
                print('{: ^36}'.format('Somente numeros'))
        else:
            print('{: ^36}'.format('Operação invalida'))
