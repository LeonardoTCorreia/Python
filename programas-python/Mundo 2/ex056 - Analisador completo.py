soma_idades = 0
maior_idade = 0
mais_velho = 0
menos_20 = 0
for i in range(1, 5):
    print(f'\n{i}ª Pessoa')
    nome = str(input('\nNome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo (m/f): ')).lower()
    soma_idades += idade
    if sexo in 'mM' and idade > maior_idade:
        maior_idade = idade
        mais_velho = nome
    if sexo in 'fF' and idade < 20:
        menos_20 += 1
media = soma_idades / 4
print('\nA média de idade foi {:.1f}'.format(media))
print(f'{mais_velho} é o homem mais velho e tem {maior_idade} anos')
print(f'{menos_20} mulheres tem menos de 20 anos')

