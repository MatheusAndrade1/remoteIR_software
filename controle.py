import PySimpleGUI as sg
import platform

sg.ChangeLookAndFeel('DarkGrey4')

BAUD = ["9600", "19200", "57600", "115200"]

if platform.system().upper() == "WINDOWS":
    COMS = ["COM1", "COM2", "COM3", "COM4", "COM5", "COM6"]
else:
    COMS = ["/dev/ttyUSB0", "/dev/ttyUSB1", "/dev/ttyUSB2", "/dev/ttyUSB3", "/dev/ttyUSB4", "/dev/ttyUSB5"]


def conectar(porta1, baudRate):
    print(porta1)
    print(baudRate)
    try:
        ser = serial.Serial(porta1, baudRate)
        sg.popup_ok('Conexão realizada com sucesso!', title='Conectado')
    except:
        sg.popup_ok('A comunicação não pôde ser estabelecida!', title='Erro')


def desconectar():
    try:
        ser.close()
    except:
        pass


def main():
    form = sg.Window('Controle remoto IR',  element_justification='c', location=(500,500*9/16), icon='/home/matheus/Documents/python/mackenzie.png')
    column1 = [[sg.Text('Column 1', justification='center', size=(10,1))],
            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 1')],
            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2')],
            [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]
    layout = [
        [sg.Text('Porta serial')],
        [sg.InputCombo(values=COMS,key='porta', font=(15)),sg.InputCombo(values=BAUD,key='baud', font=(15))],
        [sg.Button(button_text='CONECTAR'),sg.Button(button_text='DESCONECTAR')],
        [sg.Text('_'  * 25)],
        [sg.Button(button_text='LIGAR/DESLIGAR', button_color='#FF0000')],
        [sg.Button(button_text='HOME'),sg.Button('RETURN')],
        [sg.Button('^')],
        [sg.Button(button_text='<-'),sg.Button(button_text='OK'),sg.Button(button_text='->')],
        [sg.Button('v')],
        [sg.Button(button_text='1'),sg.Button(button_text='2'),sg.Button(button_text='3')],
        [sg.Button(button_text='4'),sg.Button(button_text='5'),sg.Button(button_text='6')],
        [sg.Button(button_text='7'),sg.Button(button_text='8'),sg.Button(button_text='9')]
        ]
    button, values = form.Layout(layout).Read()

    while True:             # Event Loop
        event, values = form.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Go':
            form['-OUT-'].update(values['-IN-'])

        #Botões
        if event == 'CONECTAR':
            conectar(values['porta'], values['baud'])
        elif event == 'DESCONECTAR':
            desconectar()
        elif event == 'LIGAR/DESLIGAR':
            print('Pressed button LIGAR/DESLIGAR')
            #ser.Write(b"HEXCODE\n")
        elif event == 'HOME':
            print('Pressed button HOME')
        elif event == 'RETURN':
            print('Pressed button RETURN')
        elif event == 'HOME':
            print('Pressed button ^')
        elif event == '<-':
            print('Pressed button <-')
        elif event == 'OK':
            print('Pressed button OK')
        elif event == '->':
            print('Pressed button ->')
        elif event == 'v':
            print('Pressed button v')
        elif event == '^':
            print('Pressed button ^')
        elif event == '1':
            print('Pressed button 1')
        elif event == '2':
            print('Pressed button 2')
        elif event == '3':
            print('Pressed button 3')
        elif event == '4':
            print('Pressed button 4')
        elif event == '5':
            print('Pressed button 5')
        elif event == '6':
            print('Pressed button 6')
        elif event == '7':
            print('Pressed button 7')
        elif event == '8':
            print('Pressed button 8')
        elif event == '9':
            print('Pressed button 9')
    form.close()

if __name__ == '__main__':
    main()
