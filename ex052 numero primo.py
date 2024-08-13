num = int(input('Digite um numero: '))
tot = 0
for c in range (1,num+1):
    if num % c == 0:
        print('\033[32m', end='')
        tot += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO numero {} foi divisível {} vezes.'.format(num,tot))

if tot == 2:
    print('Ele É SIM um número primo.')
else:
    print('Ele NÃO é um número primo')
