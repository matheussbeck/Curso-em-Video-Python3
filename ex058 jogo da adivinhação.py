from random import randint

player = int(input('Eu sou o JARVIS,\nDesafio você a acertar o número que estou pensando.\n \nDe 0 a 10 Qual o seu palpite? '))
jarvis = randint(0,10)
tentativas = 1

while player != jarvis:
    tentativas += 1
    if player < jarvis:
        player = int(input('ERROU, é MAIOR... Tente novamente um número de 0 a 10: '))
    else:
        player = int(input('ERROU, é MENOR... Tente novamente um número de 0 a 10: '))
print('Após {} Palpites Você conseguiu, eu estava pensando no número {}'.format(tentativas,jarvis))
