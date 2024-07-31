while True:
    tabuada = int(input('Digite o numero que deseja ver a tabuada (numero negativo para parar): '))
    print()

    if tabuada < 0:
        break
    print('===' * 5)
    
    for c in range(1, 11):
        print(f'{c} X {tabuada} = {c * tabuada}')
    print('===' * 5)