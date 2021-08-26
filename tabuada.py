from PySimpleGUI import PySimpleGUI as sg
def tabuada(num):
    for c in range(1,11):
        print(f'{c} x {num} = {c * num}')

sg.theme('DarkAmber') #Selecionando Tema
layout=[
    [sg.Text('Digite Aqui o numero que deseja caucular :'),sg.Input(key='-INPUT-',size=(17,0))],  #Criando Layout da janela
    [sg.Button('Caucular'),sg.Button('Sair')],
    [sg.Output(size=(30,10),font='Arial,20')]
]
#Fazendo com que a janela seja executada
janela = sg.Window('Programa').layout(layout)
while True :
    event, values = janela.Read()
    if event ==  sg.WINDOW_CLOSED or event == 'Sair':
        break
    if event == 'Caucular':
        num = int(values['-INPUT-'])
        print(f'{tabuada(num)}')
