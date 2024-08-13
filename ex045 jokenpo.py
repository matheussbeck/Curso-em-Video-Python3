import random
#Player
p = int(input('Digite um número:\n'
              '[1] PEDRA\n'
              '[2] PAPEL\n'
              '[3] TESOURA\n'))
if p == 1:
    print('Player: PEDRA')
elif p == 2:
    print('Player: PAPEL')
elif p == 3:
    print('Player: TESOURA')
else:
    print('é só de 1 a 3 burro')

#Bot
lista = [1,2,3]
pc = random.choice(lista)
if pc == 1:
    print('Bot: PEDRA')
elif pc == 2:
    print('Bot: PAPEL')
elif pc == 3:
    print('Bot: TESOURA')

#Jokenpo
print('')
if p == pc:
    print('EMPATOU')
elif p == 1 and pc == 2:
    print('VOCÊ PERDEU')
elif p == 1 and pc == 3:
    print('VOCÊ GANHOU')
elif p == 2 and pc == 3:
    print('VOCÊ PERDEU')
elif p == 2 and pc == 1:
    print('VOCÊ GANHOU')
elif p == 3 and pc == 1:
    print('VOCÊ PERDEU')
elif p == 3 and pc == 2:
    print('VOCÊ GANHOU')
else:
    print(':)')
