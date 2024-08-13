resp = 'S'
s = c = med = maior = menor = 0

while resp in 'Ss':
    n = int(input('Digite um número: '))
    c += 1
    s += n
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar ? [S/N] - ')).strip().lower()[0]
med = s / c
print('Você digitou {} números e média deles foi {:.2f}'.format(c,med))
print('O maior valor digitado foi {} e o menor valor foi {}.'.format(maior,menor))
