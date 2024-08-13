from math import factorial
n = int(input('Digite um número para ver o seu Fatorial: '))
f = factorial(n)
cont = n
while True:
    print(cont, 'x ',end='')
    cont -= 1
    if cont == 1:
        print(cont, '= ', f)
        break
print(f'O fatorial de {n} é {f}.')
