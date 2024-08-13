print('GERADOR DE PA\n')
n = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
c = 0
pa = 0
while True:
    pa = n + r*c
    print(pa, '> ', end='')
    c += 1
    if c == 10:
        break
print('Acabou!')
