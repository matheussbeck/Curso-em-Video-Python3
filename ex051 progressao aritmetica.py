t = int(input('Qual o primeiro termo? '))
r = int(input('Qual a razão aritmetica? '))

for c in range(t,t+r*10,r):
    print(c, end=(' > '))
print ('FIM')
