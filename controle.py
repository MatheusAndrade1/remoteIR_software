import PySimpleGUI as sg
import platform
import serial
import os
import sys
import yaml

image_onoff = 'C:\\Users\\mathe\\Documents\\TV Digital\\remoteIR_software\\image_onoff.png'
image_icon = 'C:\\Users\\mathe\\Documents\\TV Digital\\remoteIR_software\\mackenzie.ico'

sg.ChangeLookAndFeel('DarkGrey4')

BAUD = ["9600", "19200", "57600", "115200"]

if platform.system().upper() == "WINDOWS":
    COMS = ["COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8"]
else:
    COMS = ["/dev/ttyUSB0", "/dev/ttyUSB1", "/dev/ttyUSB2", "/dev/ttyUSB3", "/dev/ttyUSB4", "/dev/ttyUSB5"]

with open(r'c:\\Users\\mathe\\Documents\\TV Digital\\YAML\\default.yaml') as file:
    dictionary = yaml.load(file, Loader=yaml.FullLoader)


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def stringFormatter(hex, iten):
    try:
        newstring = hex['hexCodes'][iten].replace(" ","")
        return newstring.replace("0x","\\") + '\\n'
    except:
        return ''

def main():
    form = sg.Window('Controle remoto IR',  element_justification='c', location=(500,500*9/16), icon=resource_path('mackenzie.ico'))
    bt = {'size':(5,1), 'font':('Franklin Gothic Book', 10), 'button_color':("black","#F8F8F8")}
    bt2 = {'size':(10,1), 'font':('Franklin Gothic Book', 8), 'button_color':("black","#F8F8F8")}
    bt3 = {'size':(12,1), 'font':('Franklin Gothic Book', 8), 'button_color':("black","#F8F8F8")}
    bt4 = {'size':(6,2), 'font':('Franklin Gothic Book', 8), 'button_color':("black","#F8F8F8")}
    ic = {'size':(8,1), 'font':('Franklin Gothic Book', 10)}
    btA = {'size':(5,1), 'font':('Franklin Gothic Book', 8)}

    layout = [
        [sg.Text('Porta serial', font=16)],
        [sg.InputCombo(values=COMS,key='porta', default_value=dictionary['config']['COM'], **ic),sg.InputCombo(values=BAUD,key='baud', default_value=dictionary['config']['baudrate'], **ic)],
        [sg.Button(button_text='CONECTAR', **bt3),sg.Button(button_text='DESCONECTAR', **bt3)],
        [sg.Text('_'  * 20)],
        [sg.Button(button_color=(sg.theme_background_color()), image_filename=resource_path('image_onoff.png'), image_subsample=2, border_width=0)],
        [sg.Button(button_text='HOME', **bt2),sg.Button('SOURCE', **bt2)],
        [sg.Button(button_text='MUTE', **bt2),sg.Button('SPACE', **bt2)],
        [sg.Button(button_text='1', **bt),sg.Button(button_text='2', **bt),sg.Button(button_text='3', **bt)],
        [sg.Button(button_text='4', **bt),sg.Button(button_text='5', **bt),sg.Button(button_text='6', **bt)],
        [sg.Button(button_text='7', **bt),sg.Button(button_text='8', **bt),sg.Button(button_text='9', **bt)],
        [sg.Button(button_text='0', **bt)],
        [sg.Button(button_text='+', **bt4),sg.Button(button_text='DEL', **bt4),sg.Button(button_text='UP', **bt4)],
        [sg.Button(button_text='-', **bt4),sg.Button(button_text='ENTER', **bt4),sg.Button(button_text='DOWN', **bt4)],
        [sg.Button(button_text='RETURN', **bt2),sg.Button('EXIT', **bt2)],
        [sg.Button('^', **bt)],
        [sg.Button(button_text='<', **bt),sg.Button(button_text='OK', **bt),sg.Button(button_text='>', **bt)],
        [sg.Button('v', **bt)],
        [sg.Button(button_text='A', button_color=('white','#FF0000'), **btA),sg.Button(button_text='B', button_color=('white','#008000'), **btA),sg.Button(button_text='C', button_color=('white','#FFFF00'), **btA),sg.Button(button_text='D', button_color=('white','#0000FF'), **btA)],
        [sg.Button(button_text='LANGUAGE', **bt2),sg.Button(button_text='SEARCH', **bt2)]
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
             try:
                ser = serial.Serial(values['porta'], values['baud'])
                ser.isOpen()
                sg.popup_ok('Conexão realizada com sucesso!', title='Conectado')
             except:
                sg.popup_ok('A comunicação não pôde ser estabelecida!', title='Erro')
        try:
            if ser.isOpen():
                if event == 'DESCONECTAR':
                    try:
                        ser.close()
                    except:
                        pass
                elif event == 'HOME':
                    print('Pressed button HOME')
                    ser.write(stringFormatter(dictionary,'HOME'))
                elif event == 'SOURCE':
                    print('Pressed button SOURCE')
                    ser.write(stringFormatter(dictionary,'SOURCE'))
                elif event == 'MUTE':
                    print('Pressed button MUTE')
                    ser.write(stringFormatter(dictionary,'MUTE'))
                elif event == 'SPACE':
                    print('Pressed button SPACE')
                    ser.write(stringFormatter(dictionary,'SPACE'))
                elif event == '1':
                    print('Pressed button 1')
                    ser.write(stringFormatter(dictionary,'1'))
                elif event == '2':
                    print('Pressed button 2')
                    ser.write(stringFormatter(dictionary,'2'))
                elif event == '3':
                    print('Pressed button 3')
                    ser.write(stringFormatter(dictionary,'3'))
                elif event == '4':
                    print('Pressed button 4')
                    ser.write(stringFormatter(dictionary,'4'))
                elif event == '5':
                    print('Pressed button 5')
                    ser.write(stringFormatter(dictionary,'5'))
                elif event == '6':
                    print('Pressed button 6')
                    ser.write(stringFormatter(dictionary,'6'))
                elif event == '7':
                    print('Pressed button 7')
                    ser.write(stringFormatter(dictionary,'7'))
                elif event == '8':
                    print('Pressed button 8')
                    ser.write(stringFormatter(dictionary,'8'))
                elif event == '9':
                    print('Pressed button 9')
                    ser.write(stringFormatter(dictionary,'9'))
                elif event == '0':
                    print('Pressed button 0')
                    ser.write(stringFormatter(dictionary,'0'))
                elif event == '+':
                    print('Pressed button +')
                    ser.write(stringFormatter(dictionary,'+'))
                elif event == '-':
                    print('Pressed button -')
                    ser.write(stringFormatter(dictionary,'-'))
                elif event == 'DEL':
                    print('Pressed button DEL')
                    ser.write(stringFormatter(dictionary,'DEL'))
                elif event == 'SEARCH':
                    print('Pressed button SEARCH')
                    ser.write(stringFormatter(dictionary,'SEARCH'))
                elif event == 'UP':
                    print('Pressed button UP')
                    ser.write(stringFormatter(dictionary,'CHANNEL_UP'))
                elif event == 'DOWN':
                    print('Pressed button DOWN')
                    ser.write(stringFormatter(dictionary,'CHANNEL_DOWN'))
                elif event == 'RETURN':
                    print('Pressed button RETURN')
                    ser.write(stringFormatter(dictionary,'RETURN'))
                elif event == 'EXIT':
                    print('Pressed button EXIT')
                    ser.write(stringFormatter(dictionary,'EXIT'))
                elif event == 'ENTER':
                    print('Pressed button ENTER')
                    ser.write(stringFormatter(dictionary,'ENTER'))
                elif event == '^':
                    print('Pressed button ^')
                    ser.write(stringFormatter(dictionary,'UP'))
                elif event == '<':
                    print('Pressed button <')
                    ser.write(stringFormatter(dictionary,'LEFT'))
                elif event == 'OK':
                    print('Pressed button OK')
                    ser.write(stringFormatter(dictionary,'OK_INFO'))
                elif event == '>':
                    print('Pressed button >')
                    ser.write(stringFormatter(dictionary,'RIGHT'))
                elif event == 'v':
                    print('Pressed button v')
                    ser.write(stringFormatter(dictionary,'DOWN'))
                elif event == 'A':
                    print('Pressed button RED')
                    ser.write(stringFormatter(dictionary,'RED'))
                elif event == 'B':
                    print('Pressed button GREEN')
                    ser.write(stringFormatter(dictionary,'GREEN'))
                elif event == 'C':
                    print('Pressed button YELLOW')
                    ser.write(stringFormatter(dictionary,'YELLOW'))
                elif event == 'D':
                    print('Pressed button BLUE')
                    ser.write(stringFormatter(dictionary,'BLUE'))
                elif event == 'LANGUAGE':
                    print('Pressed button LANGUAGE')
                    ser.write(stringFormatter(dictionary,'LANGUAGE'))
                else:
                    print('Pressed button LIGAR/DESLIGAR')
                    ser.write(stringFormatter(dictionary,'ON_OFF'))
            else:
                sg.popup_ok('Não conectado!', title='Erro')
        except:
            sg.popup_ok('Não conectado!', title='Erro')
    form.close()

if __name__ == '__main__':
    main()
