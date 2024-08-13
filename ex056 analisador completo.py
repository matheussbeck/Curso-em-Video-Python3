idades = 0
maiorhomem = 0
nomevelho = ''
totmulher20 = 0
for cad in range(1,5):
    print('-'*5,'{}ª PESSOA'.format(cad),'-'*5)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).strip()
    idades += idade
    if cad == 1 and sexo in 'Mm':
        maiorhomem = idade
        nomevelho = nome
    if sexo in 'Mm' and idade > maiorhomem:
        maiorhomem = idade
        nomevelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
media = idades/cad
print('A média das idades é {} anos'.format(media))
print('O homem mais velho tem {} anos e seu nome é {}'.format(maiorhomem,nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(totmulher20))