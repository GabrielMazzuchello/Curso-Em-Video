velocidade = int(input('Informe sua atual velocidade!: '))
if velocidade > 80:
    print('Você ultrapasou a velocidade maxima permitida!!')
    print('O valor da sua multa foi de R$:{}'.format((velocidade-80)*7))
else:
    print('Você esta dentro da velocidade permitida -> 80km/h')
