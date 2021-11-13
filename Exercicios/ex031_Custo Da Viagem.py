distancia = float(input('informe a distancia da sua viagem (km)'))
if distancia > 200:
    print('O valor de sua viagem custara R$:{:.2f}'.format(distancia*0.45))
else:
    print('O valor de sua viagem custará R$:{:.2f}'.format(distancia*0.50))
