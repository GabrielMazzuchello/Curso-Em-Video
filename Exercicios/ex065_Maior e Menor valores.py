soma = contador = maior = menor = 0
while True:
    numero = int(input('Informe um valor inteiro: '))
    opcao = str(input('Quer continuar? (S/N)')).upper().strip()[0]
    soma += numero
    contador += 1
    if contador == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
    
    if opcao == 'N':
        media = soma / contador
        print('A média dos numeros digitados é de {} o maior numero digitado foi {} e o menor foi {}'.format(media, maior, menor))
        break
