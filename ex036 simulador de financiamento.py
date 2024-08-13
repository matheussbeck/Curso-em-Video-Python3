print('-='*20)
print('ANÁLISE DE FINANCIAMENTO BANCÁRIO')
print('-='*20)

#Questionário
casa = float(input('Qual o valor do imóvel a ser financiado ? R$'))
salário = float(input('Qual o seu salário atual ? R$'))
prazo = int(input('Em quantas parcelas você pretende financiar ? '))
parcela = casa/prazo
aprovado = ((salário*0.3)*prazo)
parcelaok = aprovado/prazo

#APROVADO / NEGADO
if parcela <= (salário*0.3):
    print('O seu financiamento foi \033[32mAPROVADO\033[m. Você pagará {} parcelas de R${:.2f}'.format(prazo,parcelaj))
else:
    print('O seu financiamento foi \033[31mNEGADO\033[m, porém, podemos te oferecer R${:.2f} em {} parcelas de R${:.2f}'.format(aprovado,prazo,parcelaok))

print('O que acha dessas condições ? ')
