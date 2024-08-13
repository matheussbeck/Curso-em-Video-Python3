v=int(input('Digite a velocidade do Carro: '))
l=int(input('Qual o limite da via? '))
if v>l:
    print('Ta achando que é o Rubinho? Toma aqui essa multa no valor de R$ {:.2f} de presente.'.format((v-l)*7))
else:
    print('Você está dentro do limite, Boa Viagem !')
