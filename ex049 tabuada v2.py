n = int(input('Qual numero você quer a tabuada ? '))

for c in range(0,11):
   print('{} x {:2} = {}'.format( n, c, n*c))
print('FIM')