import random
n=int(random.randint(0,5))
r=int(input('Qual número entre 0 e 5 eu estou pensando Sherlock? '))
if n==r:
    print('Parabens você acertou!')
else:
    print('Você errou my little friend! Estava pensando em {}'.format(n))
