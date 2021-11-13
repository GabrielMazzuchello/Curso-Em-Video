l = float(input('qual e a largura da sua parede?'))
h = float(input('qual e a altura da sua parede?'))
a = l * h
print('a sua parede {}X{} tem {}m² de area!'.format(l, h, a))
print('será nessesario {}L de tinta para pintar essa parede'.format(a/2))
