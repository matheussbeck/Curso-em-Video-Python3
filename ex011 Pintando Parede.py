alt=float(input('Qual a altura da parede? '))
lar=float(input('Qual a largura da parede? '))
tinta=float(input('Quantos metros são pintados com 1 litro da sua tinta ? '))
area=alt*lar
lit=area/tinta
print('Considerando uma parede de {} m², você vai precisar de {:.1f} litros de tinta'.format(area,lit))
