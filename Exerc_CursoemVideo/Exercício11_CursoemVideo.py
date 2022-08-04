lp = float(input('Largura da parede: '))
ap = float(input('Altura da parede: '))
print('Sua parede tem a dimensão de {}x{} e sua área é de {} m2'.format(lp,ap,(lp*ap)))
print('Para pintar essa parede, você precisará de %.2f L de tinta' %((lp*ap)*0.5))