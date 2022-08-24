from random import choice
from time import sleep
print('{:=^40}'.format('PEDRA,PAPEL OU TESOURA '))
sleep(1)
jogador = str(input('Digite sua escolha : '))
lista=['pedra','papel','tesoura']
computador =choice(lista)
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!')
sleep(1)
print('-=-'*40)
j = jogador.upper()
c = computador.upper()
print('O JOGADOR JOGOU {}'.format(j))
print('O COMPUTADOR JOGOU {}'.format(c))
print('-=-'*40)
if computador == 'pedra':
    if jogador == 'pedra' :
        print('EMPATE!!')
    elif jogador == 'papel' :
        print('O JOGADOR VENCEU!!')
    elif jogador == 'tesoura' :
        print('O COMPUTADOR VENCEU!!')
    else:
        print('JOGADA INVALIDA!!')
elif computador == 'papel' :
    if jogador == 'papel' :
        print('EMPATE!')
    elif jogador == 'pedra' :
        print('O COMPUTADOR VENCEU!!')
    elif jogador == 'tesoura' :
        print('O JOGADOR VENCEU!!')
    else:
        print('JOGADA INVALIDA!!')
elif computador == 'tesoura' :
    if jogador == 'tesoura' :
        print('EMPATE!!')
    elif jogador == 'pedra' :
        print('O JOGADOR VENCEU!!')
    elif jogador == 'papel':
        print('O JOGADOR VENCEU!!')
    else:
        print('JOGADA INVALIDA')
        

    
