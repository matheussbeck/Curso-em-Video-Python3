from time import sleep
n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
r = 0

while r != 5:
    print('   [ 1 ] Somar\n   [ 2 ] multiplicar\n   [ 3 ] maior\n   [ 4 ] novos números\n   [ 5 ] sair do programa')
    r = int(input('>>>>> Qual é a opção desejada? '))
    if r == 1:
        print('A opção escolhida foi [1] SOMAR')
        print('{} + {} = {}\n'.format(n1,n2,n1+n2))
    elif r == 2:
        print('A opção escolhida foi [2] MULTIPLICAR')
        print('{} x {} = {}\n'.format(n1,n2,n1*n2))
    elif r == 3:
        print('A opção escolhida foi [3] MAIOR')
        if n1 > n2:
            print('O maior número é {}\n'.format(n1))
        elif n1 < n2:
            print('O maior número é {}\n'.format(n2))
        else:
            print('Os dois são iguais\n')
    elif r == 4:
        print('A opção escolhida foi [4] NOVOS NÚMEROS')
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo Valor: '))
    elif r == 5:
        print('Finalizando o Programa !')
    else:
        print('Opção inválida, tente uma opção válida: ')
    print('=-=' * 10)
    sleep (1)
print('Até mais !')