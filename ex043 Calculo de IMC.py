print('-='*20)
print('CALCULE O SEU IMC')
print('-='*20)

p = float(input('Qual o seu peso atual? '))
a = float(input('Qual a sua altura ? '))
imc = p/(a*2)

print('Seu IMC é {:.2f}'.format(imc))
if imc > 40:
    print('Isso significa OBESIDADE MÓRBIDA')
elif imc > 30:
    print('Isso significa OBESIDADE')
elif imc > 25:
    print('Isso significa SOBREPESO')
elif imc >= 18.5:
    print('Isso significa PESO IDEAL')
else:
    print('Isso significa ABAIXO DO PESO')
