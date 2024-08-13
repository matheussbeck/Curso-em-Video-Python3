frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
print('{} Normal\n{} Invertido'.format(junto, inverso))
if inverso == junto:
    print('Essa frase é um PALÍNDROMO')
else:
    print('Essa frase NÃO É um palíndromo')
