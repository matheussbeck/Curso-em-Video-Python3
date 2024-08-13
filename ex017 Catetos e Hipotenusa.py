import math
'''co = float(input("Qual o comprimento do cateto oposto ? "))
ca = float(input('Qual o comprimento do cateto adjacente ? '))
hi = math.sqrt((co**2)+(ca**2))'''
co = float(input("Qual o comprimento do cateto oposto ? "))
ca = float(input('Qual o comprimento do cateto adjacente ? '))
hi = math.hypot(ca,co)
print('Considerando um triângulo retângulo as suas medidas são :\ncateto oposto {}\ncateto adjacente {}\nhipotenusa {}'.format(co,ca,hi))
