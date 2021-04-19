import PySimpleGUI as sg
import platform

image_onoff = 'image_onoff.png'

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
    bt = {'size':(3,1), 'font':('Franklin Gothic Book', 24), 'button_color':("black","#F8F8F8")}
    bt2 = {'size':(8,1), 'font':('Franklin Gothic Book', 16), 'button_color':("black","#F8F8F8")}
    bt3 = {'size':(12,1), 'font':('Franklin Gothic Book', 13), 'button_color':("black","#F8F8F8")}
    ic = {'size':(8,1), 'font':('Franklin Gothic Book', 16)}

    layout = [
        [sg.Text('Porta serial', font=16)],
        #[sg.InputCombo(values=COMS,key='porta', font=(15)),sg.InputCombo(values=BAUD,key='baud', font=(15))],
        [sg.InputCombo(values=COMS,key='porta', default_value='COM4', **ic),sg.InputCombo(values=BAUD,key='baud', default_value='9600', **ic)],
        [sg.Button(button_text='CONECTAR', **bt3),sg.Button(button_text='DESCONECTAR', **bt3)],
        [sg.Text('_'  * 30)],
        #[sg.Button(image_filename=image_onoff, **btpower)],
        [sg.Button(button_color=(sg.theme_background_color(), sg.theme_background_color()), image_filename=image_onoff, image_subsample=2, border_width=0)],
        [sg.Button(button_text='HOME', **bt2),sg.Button('RETURN', **bt2)],
        [sg.Button('^', **bt)],
        [sg.Button(button_text='<', **bt),sg.Button(button_text='OK', **bt),sg.Button(button_text='>', **bt)],
        [sg.Button('v', **bt)],
        [sg.Button(button_text='1', **bt),sg.Button(button_text='2', **bt),sg.Button(button_text='3', **bt)],
        [sg.Button(button_text='4', **bt),sg.Button(button_text='5', **bt),sg.Button(button_text='6', **bt)],
        [sg.Button(button_text='7', **bt),sg.Button(button_text='8', **bt),sg.Button(button_text='9', **bt)]
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
            #ser.Write(b"HEXCODE\n")
        elif event == 'HOME':
            print('Pressed button HOME')
        elif event == 'RETURN':
            print('Pressed button RETURN')
        elif event == 'HOME':
            print('Pressed button ^')
        elif event == '<':
            print('Pressed button <')
        elif event == 'OK':
            print('Pressed button OK')
        elif event == '>':
            print('Pressed button >')
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
        else:
            print('Pressed button LIGAR/DESLIGAR')
    form.close()

if __name__ == '__main__':
    main()
