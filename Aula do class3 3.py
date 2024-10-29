nome = str(input('digite um nome: '))
gab = len (nome)
if(gab <= 3):
 print("valido",gab)
else:
 print("invalido")
idade=int(input('digite sua idade: '))
if(idade>=0)and(idade<=150):
 print("valido",idade)
else:
 print("invalido")
salario=int(input("informe seu salario: "))
if(salario>0):
 print("valido",salario)
else:
 print("invalido")
sexo=str(input("informe seu sexo: "))
if(sexo=="m")or(sexo=="f"):
 print("valido",sexo)
else:
 print("invalido")
estadocivil=str(input("informe seu estado civil: "))
if(estadocivil=="s")or(estadocivil=="c")or(estadocivil=="v")or(estadocivil=="d"):
 print("valido",estadocivil)
else:
 print("invalido")