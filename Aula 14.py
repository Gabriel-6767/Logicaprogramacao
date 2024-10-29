par = 0
impar = 0
for i in range(10):
    n1 = int(input('informe um número: '))
    if(n1 % 2 == 0):
        par = par + 1
        print('o número é par: ')
        print(par)
    else:
        print('o número é impar: ')
        impar = impar + 1