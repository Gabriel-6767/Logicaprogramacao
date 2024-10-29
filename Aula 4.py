# 2)escreva um programa que receba dois valores para as variáveis x e y. Depois, troque os valores (utilizando 3 variáveis)  e exiba-os na tela.
x = int(input('valor de x: '))
y = int(input('valor de y: '))
troca = x
x = y
y = troca
print(x)
print(y)
