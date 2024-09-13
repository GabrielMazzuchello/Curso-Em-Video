print('='*30)
print('{:^30}'.format('Banco CEV'))
print('='*30)

Valor = int(input('informe o valor que deseja sacar R$: '))

total = Valor

cedula = 50
totalCedula = 0
while True:
    if total >= cedula:
        total -= cedula
        totalCedula += 1
    else:
        if totalCedula > 0:
            print(f'Total de {totalCedula} de {cedula}')
        
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1

        totalCedula = 0
        if total == 0:
            break