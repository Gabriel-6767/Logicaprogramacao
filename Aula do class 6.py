fora = 0 
ponto = 0
for i in range(1,5):
    n = int(input('digite um número: '))
    if(n <= 0):
        ponto = ponto + 1
    else:
        fora = fora + 1
print('existem {} números negativos'.format(ponto))