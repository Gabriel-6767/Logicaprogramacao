i = 1
curry = 0 
lebron = 0
durant = 0
luka = 0 
while(i > 0):
    n = int(input('digite um número: '))
    if(n > 0) and (n < 25):
        curry += 1
    if(n >= 26) and (n <= 50):
        lebron += 1
    if(n >= 51) and (n <= 75):
        durant += 1
    if(n >= 76) and (n <= 100):
        luka += 1 
    if(n < 0):
        print('invalido')
        i = -1
print('dentro do intervalo [0,25]', curry)
print('dentro do intervalo [26,50]', lebron)
print('dentro do intervalo [51,75]', durant)
print('dentro do intervalo [76,100]', luka)