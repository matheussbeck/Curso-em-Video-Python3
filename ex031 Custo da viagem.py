d = int(input('Qual a distância da sua viagem ? '))
if d>200:
    print('O valor da sua passagem é R$ {:.2f}'.format(d*0.45))
else:
    print('O valor da sua passagem é R${:.2f}'.format(d*0.50))
