# faça um programa que receba a idade, altura e o peso de 25 pessoas e mostre:
# a quantidade de pessoas com superior a 50 anos.
i = 0 
maior = 0
menor = 0
while(i < 3):
    i += 1
    idade = int(input('informe uma idade: '))
    altura = float(input('informe uma altura: '))
    peso = float(input('informe um peso: '))
    if(idade > 50):
        maior = maior + 1
    else:
        menor = menor+ 1 
print('maiores que 50 anos',maior)
print('menores que 50 anos',menor)
