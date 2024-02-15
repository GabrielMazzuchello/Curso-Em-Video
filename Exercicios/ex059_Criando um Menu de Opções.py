n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))

opcao = 0
while opcao != 5:
    print('''        [ 1 ] Somar
        [ 2 ] Multiplicar
        [ 3 ] Maior
        [ 4 ] Novos números
        [ 5 ] Sair do programa''')
    opcao = int(input('Qual é a sua opção? '))

    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} + {} é {}'.format(n1, n2, soma))

    elif opcao == 2:
        multiplicacao = n1 * n2
        print('A multiplicação entre {} X {} é {}'.format(n1, n2, multiplicacao))

    elif opcao == 3:
        if n1 > n2:
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, n2))
        elif n2 > n1:
            print('Entre {} e {} o maior valor é {}'.format(n1, n2, n2))
        elif n1 == n2:
            print('Os números {} e {} são iguais'.format(n1, n2))

    elif opcao == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))

    elif opcao == 5:
        print('Finalizando')

    else:
        print('Opção invalida tente novamente!')
    print('=-=' * 10)
print('Fim do programa! volte sempre!')
