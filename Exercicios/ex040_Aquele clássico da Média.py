nota1 = float(input('informe a 1° nota do aluno: '))
nota2 = float(input('Informe a 2° nota do aluno: '))
media = (nota1 + nota2) / 2

print('')
print('A media do aluno foi de {:.1f}'.format(media))
if media >= 7:
    print('PARABENS!! Você foi {}aprovado{}.'.format('\033[34m', '\033[m'))
elif media >= 5 and media < 7:
    print('Que pena, você precisará fazer {}recuperação{}!'.format('\033[33m', '\033[m'))
elif media < 5:
    print('Que pena, estude mais na proxima você foi {}REPROVADO{}!!!'.format('\033[31m', '\033[m'))
