maior = 0
maior2 = 0
maior3 = 0

menor = 0
menor2 = 0
menor3 = 0
for i in range(1,5):
    idade = int(input('informe uma idade: '))
    peso = int(input('informe um peso: '))
    altura = float(input('informe uma altura: '))

    if(i == 1):
        maior = idade
        maior2 = peso
        maior3 = altura
        
        menor = idade
        menor2 = peso
        menor3 = altura

    else:
        if idade > maior:
            maior = idade
        if peso > maior2:
            maior2 = peso
        if altura > maior3:
            maior3 = altura

        if idade < menor:
            menor = idade
        if peso < menor2:
            menor2 = peso
        if altura < menor3:
            menor3 = altura

print('{} idade maior'.format(maior))
print('{} peso maior'.format(maior2))
print('{} altura maior'.format(maior3))
print('{} idade menor'.format(menor))
print('{} peso menor'.format(menor2))
print('{} altura menor'.format(menor3))






