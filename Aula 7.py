# Escreva um programa que receba trê notas, mostre a média aritmética delas e informe se o aluno foi aprovado ou reprovado. 
# Nota para ser aprovado deve ser igual ou maior que 7.
n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
n3 = float(input('Nota 3: '))
Nota = (n1 + n2 + n3)/3
if(Nota > 7):
    print('aluno foi aprovado')
else:
    print('aluno foi reprovado')