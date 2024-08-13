p=float(input('Qual o preço do produto? '))
d=float(input('Qual o Percentual de desconto a ser aplicado? '))
np=p*(1-d/100)
print('De R${:.2f} o produto está saindo por R${:.2f}'.format(p,np))
