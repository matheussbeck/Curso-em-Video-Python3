print('-='*20)
print('ANALISADOR DE TRIANGULOS')
print('-='*20)

r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))

if r1 < r2+r3 and r2 < r1+r3 and r3 <r1+r2:
    print('Suas retas formam um Triângulo')
else:
    print('Suas retas NÃO formam um Triângulo')
