sexo = input(str('Qual é seu sexo M ou F? ')).strip().upper()

while sexo not in 'MmFf':
    print('Não aceitamos esse caracter! Por favor digite (F ou M)')
    sexo = str(input('Digite seu sexo ')).upper().strip()

print('Seu sexo {} foi registrado com sucesso!'.format(sexo))
