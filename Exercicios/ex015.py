di = int(input('quantos dias o carro foi alugado?'))
km = float(input('quantos km o carro percorreu?'))
total = (km * 0.15) + (di * 60)
print('o aluguel do carro custou R${:.2f}'.format(total))
