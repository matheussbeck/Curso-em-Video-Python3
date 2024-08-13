i = int(input('Qual a sua idade ? '))
t = 18-i

if i == 18:
    print('Já está na hora de se alistar camarada')
elif i < 18:
    print('Paciencia camarada ainda faltam {} anos para o seu alistamento'.format(t*1))
else:
    print('Camarada você já está {} anos atrasado para o seu alistamento'.format(t*-1))
print('Boa sorte')
