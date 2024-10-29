n1=int(input("informe um numero inteiro: "))
if(n1>1):
    for i in range(2,n1):
        if(n1%i==0):
            print("nao e um numero primo")
            break
        else:
            print("é um número primo")
            break
else:
    print("nao e um numero primo")