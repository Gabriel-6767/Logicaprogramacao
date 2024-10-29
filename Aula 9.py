#escreva um programa que leia o código de origem de um produto e imprima na tela e região de sua procedência.
r = int(input('informe um código: '))
if(r == 1):
    print('sul')
if(r == 2):
    print('norte')
if(r == 3):
    print('leste')
if(r == 4):
    print('oeste')
if(r == 5) or (r == 6):
    print('nordeste')
if(r == 7) or (r == 8) or (r == 9):
    print('sudeste')
if(r == 10):
    print('centro-oeste')
if(r == 11):
    print('nordeste')
if(r > 11):
    print('não é um código seu burro!')