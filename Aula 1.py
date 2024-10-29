n1 = float(input("digite um valor: "))


nome = str(input('informe o seu nome: '))


bool


x = int(input('valor de x: '))
y = int(input('valor de x: '))
troca = x
x = y
y = troca
print(x)
print(y)



codigo = int(input('digite o codigo de verificação'))
num1 = int(input('digite o total de vendas'))
if(num1 > 10):
    print('a comisão aumentou 0%')
elif(num1 > 100) and (num1 < 350):
    print('a comisão aumentou 6%')
    som = (num1 / 6)+ num1
    print(som)
elif(num1 > 350):
    print('a comisão aumentou 10%')
    som = (num1 / 10) + num1
    print(som)




n1 = int(input('digiteum número inteiro'))
if(n1 > 1):
    print('o número é positivo')
    if(n1 % 2 == 0):
        print('o número é par')
    else:
        print('o número é impar')
else:
    print('valor negativo')




for i in range(30):
    print(i)



