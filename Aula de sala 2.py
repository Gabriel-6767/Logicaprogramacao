i = 0 
maior = 0
maior2 = 0
maior3 = 0
maior4 = 0
menor = 0
while (i < 3):
    messi = int(input('digite um número: '))
    if(messi > 0) and (messi < 25):
        maior += 1
    if(messi > 26) and (messi < 50):
        maior2 += 1
    if(messi > 51) and (messi < 75):
        maior3 += 1
    if(messi > 76) and (messi < 100):
        maior4 += 1 
if(messi < 0 ):
    print('erro')
print('dentro do intervalo[0,25]', maior)
print('dentro do intervalo[26,50]', maior2)
print('dentro do intervalo[51,75]', maior3)
print('dentro do intervalo [76,100]', maior4)


