sal = float(input('Qual o valor do seu salário ? R$'))
if sal<=1250:
    print('Você recebeu 15% de aumento salarial, seu novo salário é R${:.2f}'.format(sal*1.15))
else:
    print('Você recebeu 10% de aumento salárial, seu novo salário é {:.2f}'.format(sal*1.1))
