primeiro = int(input('Primeiro termo: '))
razao = int(input('Informe a razao: '))
decimo = primeiro + (10 - 1) * razao

for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end=' -> ')
print('FIM')
