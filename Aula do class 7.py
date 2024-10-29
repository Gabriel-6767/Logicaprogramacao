for i in range(150):
    nome = str(input("Informe o nome: "))
    endereco = str(input('Informe o endereco: '))
    compras = float(input('Informe um valor das compras: '))
if(compras <= 50.000):
    bonus = compras * 1.10
    print('seu bonus é de',bonus)
    print(nome)
    print(endereco)
    print(compras)
else:
    bonus = compras * 1.15
    print('seu bonus é de',bonus)
    print(nome)
    print(endereco)
    print(compras)