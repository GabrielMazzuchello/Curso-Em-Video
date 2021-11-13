from math import radians, sin, cos, tan

angulo = float(input('Digite o valor do angulo desejado: '))

print('')
seno = sin(radians(angulo))
print('o seno do angulo {}° É> {:.2f}'.format(angulo, seno))
cosseno = cos(radians(angulo))
print('O cosseno do angulo {}° É> {:.2f}'.format(angulo, cosseno))
tangente = tan(radians(angulo))
print('À tangente o ângulo {}° É> {:.2f}'.format(angulo, tangente))
