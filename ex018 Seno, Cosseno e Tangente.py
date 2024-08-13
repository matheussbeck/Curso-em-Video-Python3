from math import radians,sin,cos,tan
Angulo = float(input('Digite o Angulo: '))
seno = sin(radians(Angulo))
cosseno = cos(radians(Angulo))
tangente = tan(radians(Angulo))
print ('considerando o Angulo de {}, o Seno é {:.2f}, o Cosseno é {:.2f} e a Tangente {:.2f}'.format(Angulo,seno,cosseno,tangente))
