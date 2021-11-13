nome = str(input('Informe o nome do aluno: '))
nota1 = float(input('Informe a 1° nota: '))
nota2 = float(input('Informe a 2° nota: '))
nota3 = float(input('Informe a 3° nota: '))
media = (nota1 + nota2 + nota3) / 3

print('A media do aluno: {} é de {:.2f}'.format(nome, media))
