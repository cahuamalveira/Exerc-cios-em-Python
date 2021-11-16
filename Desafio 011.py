med1 = float (input ('Qual a altura da parede? Em metros '))
med2 = float (input ('Qual a largura da sua parede? Em metros'))
area = med1 * med2
tinta = area / 2
print ('Já que a área é {}m², serão necessários {} baldes de tinta para  {}m² de parede' .format (area, tinta, area))