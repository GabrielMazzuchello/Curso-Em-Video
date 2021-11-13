from datetime import date
nascimento = int(input('Informe o ano de nacimento: '))
ano = date.today().year
idade = ano - nascimento

print('')
print('A idade do atleta é {} ano(S)'.format(idade))
if idade <= 9:
    print('A categoria do atleta é MIRIM')
elif idade <= 14:
    print('A categoria do atleta é INFANTIL')
elif idade <= 19:
    print('A categoria do atleta é JÚNIOR')
elif idade <= 25:
    print('A categoria do atlrta é SÊNIOR')
else:
    print('A categoria do atleta é MASTER')
