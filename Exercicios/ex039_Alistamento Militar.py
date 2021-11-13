from datetime import date
sexo = str(input('Informe seu sexo (Feminino) ou (Masculino): ')).lower().strip()
print('')

if sexo == 'masculino':
    nacimento = int(input('informe o ano de nacimento: '))
    data = date.today().year
    idade = data - nacimento

    print('Nasceu em {} possui {} ano(S) no ano de {}'.format(nacimento, idade, data))
    print('')
    if idade < 18:
        print('Ainda faltãm {} anos para o alistamento'.format(18 - idade))
        print('O ano de alistamento é {}'.format(data + (18 - idade)))

    elif idade > 18:
        print('Você deve se alistar imidiatamente')
        print('Você já deveria ter se alistado, Se passaram {} anos'.format(idade - 18))
        print('Ano do alistamento foi {}'.format(data - (idade - 18)))
    elif idade == 18:
        print('Você deve se alistar imidiatamente')

else:
    print('Você e mulher não precisa fazer alistamento!!')
