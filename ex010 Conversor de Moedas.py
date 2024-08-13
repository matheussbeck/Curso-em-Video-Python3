c=float(input('Quantos reais você tem na sua carteira? '))
d=float(input('Qual a cotação atual do dolar ? '))
cv=c/d
print('Com R${:.2f} você pode converter para U${:.2f}'.format(c,cv))
