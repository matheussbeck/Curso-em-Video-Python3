s=float(input('Qual o seu salário atual? '))
a=float(input('Qual o percentual de aumento salarial? '))
m=s*(1+(a/100))
print('O seu salário era R${:.2f}, mas a partir do reajuste será R${:.2f}'.format(s,m))
