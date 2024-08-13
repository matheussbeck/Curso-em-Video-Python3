m1 = float(input('Primeira Nota: '))
m2 = float(input('Segunda Nota: '))
m = (m1+m2)/2
print('Sua média foi {:.2f}'.format(m))
if m >= 7:
    print('Parabens você foi \033[32mAPROVADO\033[m')
elif m >=5:
    print('Bateu na trave, você está de \033[33mRECUPERAÇÃO\033[m')
else:
    print('Burro demais, voce foi \033[31mREPROVADO\033[m')
print('Boa Sorte')
