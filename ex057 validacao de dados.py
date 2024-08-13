sexo = str(input('Informe seu sexo: [M/F] ')).upper().strip()[0]

while sexo not in 'FfMm':
    sexo = str(input('Dados invalidos. Informe seu sexo: [M/F]')).upper().strip()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))
