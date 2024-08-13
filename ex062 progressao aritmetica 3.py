print('GERADOR DE PA\n')
n = int(input('Primeiro termo: '))
r = int(input('Razão da PA: '))
c = 0
pa = 0
p = 10
total = 0
while p != 0:
    c += p
    while True:
        pa = n + r*c
        print(pa, '> ', end='')
        c += 1
        if c == 10:
            p = int(input('\nQuantos termos a mais você quer mostrar ?'))
    s = c + p
    while True:
        pa = n + r * c
        print(pa, '> ', end='')
        c += 1
        if c == s:
            break
print('Acabou!')