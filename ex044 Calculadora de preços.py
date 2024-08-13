p = float(input('Qual o valor do Produto? R$'))
c = int(input('Qual a forma de pagamento ?\n'
              ' [1] À Vista (dinheiro)\n'
              ' [2] À Vista (Cartão)\n'
              ' [3] Cartão de Crédito em 2x\n'
              ' [4] Cartão de Crédito em 3x ou mais:'))

if c == 1:
    print('Pagando em dinheiro você ganhou 10% de desconto, O Produto vai custar R${:.2f}'.format(p-(p*0.1)))
elif c == 2:
    print('Pagando a Vista no Cartão Você ganhou 5% de desconto, O produto vai custar R${:.2f}'.format(p-(p*0.05)))
elif c == 3:
    print('Parcelando em 2x no Cartão o produto vai custar R${:.2f}'.format(p))
else:
    print('Parcelando em 3x ou mais no Cartão o produto vai custar R${:.2f}'.format(p+(p*0.2)))
print ('é Noix')
