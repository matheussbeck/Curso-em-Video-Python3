print('-='*20)
print('CONVERSOR DE NUMEROS')
print('-='*20)

n = int(input('Digite um numero: '))
conv = int(input('Deseja convertê lo para:\n [1] Binário\n [2] Octal\n [3] Hexadecimal :'))

if conv == 1:
    print('binario')
elif conv == 2:
    print('Octal')
elif conv == 3:
    print('Hexadecimal')
else:
    print('A opção informada não está disponível')
