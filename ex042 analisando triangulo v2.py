print('-='*20)
print('ANALISADOR DE TRIANGULOS')
print('-='*20)

r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))

if r1 < r2+r3 and r2 < r1+r3 and r3 <r1+r2:
    print('Suas retas formam um Triângulo')
    if r1 == r2 and r1 == r3:
        print('Um triângulo do tipo Equilatero')
    elif r1 == r2 and r1 != r3 or r1 == r3 and r3 != r2 or r2 == r3 and r2 != r1:
        print('Um triângulo do tipo Isóceles')
    else:
        print('Um triângulo do tipo Escaleno')
else:
    print('Suas retas NÃO formam um Triângulo')
