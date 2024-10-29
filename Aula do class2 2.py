i = 0 
joao = 0
jose = 0
maria = 0
meunego = 0
nulo = 0 
branco = 0
while(i < 6):
    candidato = int(input('digite o código do candidato: '))
    if(candidato == 1):
        jose += 1
    if(candidato == 2):
        joao += 1
    if(candidato == 3):
        maria += 1
    if(candidato == 4):
        meunego += 1
    if(candidato == 5):
        nulo += 1
    if(candidato == 6):
        branco += 1
    if(candidato >= 7):
        print('erro')
        i = 7
soma = nulo /(jose + joao + maria + meunego) *100
soma2 = branco /(jose + joao + maria + meunego) *100
print('o total de votos que jose recebeu foi: ', jose)
print('o total de votos que joao recebeu foi: ', joao)
print('o total de votos que maria recebeu foi: ', maria)
print('o total de votos que meunego recebeu foi: ', meunego)
print('o total de votos que nulo recebeu foi: ', nulo)
print('o total de votos que branco recebeu foi: ', branco)
print('votos do branco: ', soma)
print('votos do nulo: ', soma2)