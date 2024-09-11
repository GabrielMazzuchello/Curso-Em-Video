countHomens = 0
maisDezoito = 0
mulheres = 0

while True:
    idade = int(input('Informe a idade: '))
    sexo = input('informe o sexo [F/M]: ').upper()
    print('==='*10)

    if idade > 18:
        maisDezoito += 1

    if sexo == 'M':
        countHomens += 1 

    if sexo == 'F' and idade < 20:
        mulheres += 1

    resp = '  '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if resp == 'N':
        break

print(f'Tem {maisDezoito} pessoas maiores de 18 anos')
print(f'Foram cadastrados {countHomens} homen')
print(f'Tem {mulheres} mulheres cadastradas e com menos de 20 anos')

