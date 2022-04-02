somaidade = 0
mediaidade = 0
idadevelho = 0
nomevelho = ''
mulhernova = 0

for p in range(1, 5):
    print('------ {}° PESSOA ------')

    nome = str(input('Informe seu nome: ')).strip()
    idade = int(input('Informe sua idade: '))
    sexo = str(input('informe seu Sexo [M/F]')).strip()

    somaidade += idade

    if p == 1 and sexo in 'Mm':
        idadevelho = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > idadevelho:
        idadevelho = idade
        nomevelho = nome
    if sexo in 'Ff' and idade <= 20:
        mulhernova += 1
mediaidade = somaidade / 4

print('')
print('A media de idade do grupo é de {} anos'.format(mediaidade))
print('O homen mais velho tem {} anos e su nome é {}'.format(idadevelho, nomevelho))
print('São {} mulher(es) com ou abaixo de 20 anos de idade!'.format(mulhernova))
