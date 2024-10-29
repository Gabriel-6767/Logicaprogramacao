n = 0
i = str(input('vai informar se vc é ho ou m: '))
h = float(input('informe a altura: '))
if(i == 'ho'):
    n = (72.7* h) - 58
    print(n)
if(i == 'm'):
    n =  (62.1* h) - 44.7
    print(n)
    