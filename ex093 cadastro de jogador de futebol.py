jog = dict()
gol = list()
totgol = 0
jog['nome'] = str(input('Nome: '))
jog['gols'] = gol [:]
for c in range (1,5):
    g = int(input(f'Gols na partida {c}: '))
    gol.append(g)
    c += 1
    totgol += g
jog['total'] = totgol
print('--'*30)
print(jog.items())
print('--'*30)
for k , v in jog.items():
    print(f'O campo {k} tem o valor {v}')
print('--'*30)
print(f'O jogador {jog["nome"]} jogou {c-1} partidas')
for c in range(1,5):
    print(f'Na partida {c}ª, fez {gol[c-1]} gols',end='')
    print()
print(f'Totalizando {jog["total"]} gols')