soma = 0
ponto = 0 
for i in range(1,10):
    pai = int(input('informe um número: '))
    if(10 <= pai <= 20):
        soma += 1
    else:
        ponto += 1
print('número intervalo [10,20]',soma)
print('número fora do intervalo',ponto)