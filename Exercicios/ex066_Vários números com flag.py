soma = 0
count = 0
while True:
    numero = int(input('Digite um numero inteiro [Digite 999 paar parar] -> '))
    if numero == 999:
        break
    soma += numero
    count += 1
print(f'Foram digitados {count} numeros')
print(f'A soma foi de {soma}')

