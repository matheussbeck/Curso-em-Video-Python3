cont = 0
soma = 0

while True:
    n = int(input('Digite um número [999 para parar]: '))
    cont += 1
    soma += n
    if n == 999:
        cont -= 1
        soma -= 999
        break
print('Você digitou {} números e a soma deles foi {}.'.format(cont,soma))
