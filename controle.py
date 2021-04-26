import PySimpleGUI as sg
import platform
import serial
import os
import sys
import yaml
import time

image_onoff = 'C:\\Users\\mathe\\Documents\\TV Digital\\remoteIR_software\\image_onoff.png'
image_icon = 'C:\\Users\\mathe\\Documents\\TV Digital\\remoteIR_software\\mackenzie.ico'

sg.ChangeLookAndFeel('DarkGrey4')

gif103 = b'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'

""" GLOBAL VARIABLES """
BAUD = ["9600", "19200", "57600", "115200"]

if platform.system().upper() == "WINDOWS":
    COMS = ["COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8"]
else:
    COMS = ["/dev/ttyUSB0", "/dev/ttyUSB1", "/dev/ttyUSB2", "/dev/ttyUSB3", "/dev/ttyUSB4", "/dev/ttyUSB5"]


defaultFile = {}

"""=============="""


def readYAML(path):
    """Open the specified YAML file"""
    with open(path) as file:
        return yaml.load(file, Loader=yaml.FullLoader)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

def stringFormatter(hex, iten):
    """Formats the hexcodes to send via serial to the module"""
    try:
        newstring = hex['hexCodes'][iten].replace(" ","")
        return newstring.replace("0x","\\") + '\\n'
    except:
        return ''

def getName(dictionary, iten):
    """Load config options from the dictionary"""
    if dictionary['config'][iten] is None:
        if iten=='COM':
            return 'COM7'
        else:
            return '9600'
    else:
        if iten=='COM':
            return dictionary['config']['COM']
        else:
            return dictionary['config']['baudrate']

def pretty(d, indent=0):
    """Format dictionaries to show in a box"""
    text = ""
    for key, value in d.items():
        text += ('\n' + '\t' * indent + str(key) + ': ')
        if isinstance(value, dict):
            text += pretty(value, indent+1)
        else:
            text += ('\t' * (indent+1) + str(value))
    return text

def receiveSerial(ser, iten):
    """Receive serial value, convert it to string and format"""
    ser.flushInput()
    time.sleep(.1)
    bytes_ = ser.read(25)
    text = str(bytes_)
    text = text.replace('\'','')
    text = text.replace('b','')
    return text.replace('\\n','')

def readSave(dictionaryToSave):
    """Form to load hexcodes and save them as YAML files"""
    # ------ Menu Definition ------ #      
    menu_def = [['File',['Save']]
    ] 

    form = sg.Window('Controle remoto IR',  element_justification='c', location=(500,100), icon=resource_path('mackenzie.ico'))
    bt = {'size':(5,1), 'font':('Franklin Gothic Book', 10), 'button_color':("black","#F8F8F8")}
    bt2 = {'size':(10,1), 'font':('Franklin Gothic Book', 8), 'button_color':("black","#F8F8F8")}
    bt3 = {'size':(12,1), 'font':('Franklin Gothic Book', 8), 'button_color':("black","#F8F8F8")}
    bt4 = {'size':(6,2), 'font':('Franklin Gothic Book', 8), 'button_color':("black","#F8F8F8")}
    ic = {'size':(8,1), 'font':('Franklin Gothic Book', 10)}
    btA = {'size':(5,1), 'font':('Franklin Gothic Book', 8)}

    columnLeft = [
        [sg.Text('  '), sg.Text('Porta serial', font=16), sg.Text('⬤', font=12, key='status', text_color='red')],
        [sg.InputCombo(values=COMS,key='porta', default_value=getName(dictionaryToSave, 'COM'), **ic),sg.InputCombo(values=BAUD,key='baud', default_value=getName(dictionaryToSave, 'baudrate'), **ic)],
        [sg.Button(button_text='CONECTAR', **bt3),sg.Button(button_text='DESCONECTAR', **bt3)],
        [sg.Text('_'  * 20)],
        [sg.Text('      '), sg.Button(button_color=(sg.theme_background_color()), image_filename=resource_path('image_onoff.png'), image_subsample=2, border_width=0)],
        [sg.Button(button_text='HOME', **bt2),sg.Button('SOURCE', **bt2)],
        [sg.Button(button_text='MUTE', **bt2),sg.Button('SPACE', **bt2)],
        [sg.Button(button_text='1', **bt),sg.Button(button_text='2', **bt),sg.Button(button_text='3', **bt)],
        [sg.Button(button_text='4', **bt),sg.Button(button_text='5', **bt),sg.Button(button_text='6', **bt)],
        [sg.Button(button_text='7', **bt),sg.Button(button_text='8', **bt),sg.Button(button_text='9', **bt)],
        [sg.Text('          '),  sg.Button(button_text='0', **bt)],
        [sg.Button(button_text='+', **bt4),sg.Button(button_text='DEL', **bt4),sg.Button(button_text='UP', **bt4)],
        [sg.Button(button_text='-', **bt4),sg.Button(button_text='ENTER', **bt4),sg.Button(button_text='DOWN', **bt4)],
        [sg.Button(button_text='RETURN', **bt2),sg.Button('EXIT', **bt2)],
        [sg.Text('          '), sg.Button('^', **bt)],
        [sg.Button(button_text='<', **bt),sg.Button(button_text='OK', **bt),sg.Button(button_text='>', **bt)],
        [sg.Text('          '), sg.Button('v', **bt)],
        [sg.Button(button_text='A', button_color=('white','#FF0000'), **btA),sg.Button(button_text='B', button_color=('white','#008000'), **btA),sg.Button(button_text='C', button_color=('white','#FFFF00'), **btA),sg.Button(button_text='D', button_color=('white','#0000FF'), **btA)],
        [sg.Button(button_text='LANGUAGE', **bt2),sg.Button(button_text='SEARCH', **bt2)]
    ]
    columnRight = [
        [sg.Text('Configuration file: ', font=14)],
        [sg.Multiline(pretty(dictionaryToSave), size=(50, 35), font='4', background_color='white', text_color='black', key='archive')]
    ]

    layout = [
        [sg.Menu(menu_def, tearoff=True)],
        [sg.Column(columnLeft, justification='center', vertical_alignment='center'), sg.Column(columnRight)]
    ]
    window = form.Layout(layout)

    while True:             # Event Loop
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Go':
            form['-OUT-'].update(values['-IN-'])
        #Botões
        if event == 'CONECTAR':
             try:
                ser = serial.Serial(values['porta'], values['baud'])
                sg.popup_ok('Conexão realizada com sucesso!', title='Conectado')
                form['status'].Update(text_color='green')
             except:
                form['status'].Update(text_color='red')
                sg.popup_ok('A comunicação não pôde ser estabelecida!', title='Erro')
        elif event == 'Save':
            path = sg.popup_get_file('Please enter a file name', save_as=True, default_extension='.yaml', file_types=(('YAML file', '.yaml'),))
            f = open(path, "w")
            with open(path, 'w') as file:
                documents = yaml.dump(dictionaryToSave, file)
            f.close()
        else: 
            try:
                if ser.isOpen():
                    form['status'].Update(text_color='green')
                    if event == 'DESCONECTAR':
                        try:
                            ser.close()
                            sg.popup_ok('Conexão fechada com sucesso!', title='Desconectado')
                            form['status'].Update(text_color='red')
                        except:
                            pass
                    elif event == 'HOME':
                        print('Pressed button HOME')
                        dictionaryToSave['hexCodes']['HOME'] = receiveSerial(ser, 'HOME')
                    elif event == 'SOURCE':
                        print('Pressed button SOURCE')
                        dictionaryToSave['hexCodes']['SOURCE'] = receiveSerial(ser, 'SOURCE')
                    elif event == 'MUTE':
                        print('Pressed button MUTE')
                        dictionaryToSave['hexCodes']['MUTE'] = receiveSerial(ser, 'MUTE')
                    elif event == 'SPACE':
                        print('Pressed button SPACE')
                        dictionaryToSave['hexCodes']['SPACE'] = receiveSerial(ser, 'SPACE')
                    elif event == '1':
                        print('Pressed button 1')
                        dictionaryToSave['hexCodes'][1] = receiveSerial(ser, '1')
                    elif event == '2':
                        print('Pressed button 2')
                        dictionaryToSave['hexCodes'][2] = receiveSerial(ser, '2')
                    elif event == '3':
                        print('Pressed button 3')
                        dictionaryToSave['hexCodes'][3] = receiveSerial(ser, '3')
                    elif event == '4':
                        print('Pressed button 4')
                        dictionaryToSave['hexCodes'][4] = receiveSerial(ser, '4')
                    elif event == '5':
                        print('Pressed button 5')
                        dictionaryToSave['hexCodes'][5] = receiveSerial(ser, '5')
                    elif event == '6':
                        print('Pressed button 6')
                        dictionaryToSave['hexCodes'][6] = receiveSerial(ser, '6')
                    elif event == '7':
                        print('Pressed button 7')
                        dictionaryToSave['hexCodes'][7] = receiveSerial(ser, '7')
                    elif event == '8':
                        print('Pressed button 8')
                        dictionaryToSave['hexCodes'][8] = receiveSerial(ser, '8')
                    elif event == '9':
                        print('Pressed button 9')
                        dictionaryToSave['hexCodes'][9] = receiveSerial(ser, '9')
                    elif event == '0':
                        print('Pressed button 0')
                        dictionaryToSave['hexCodes'][0] = receiveSerial(ser, '0')
                    elif event == '+':
                        print('Pressed button +')
                        dictionaryToSave['hexCodes']['+'] = receiveSerial(ser, '+')
                    elif event == '-':
                        print('Pressed button -')
                        dictionaryToSave['hexCodes']['-'] = receiveSerial(ser, '-')
                    elif event == 'DEL':
                        print('Pressed button DEL')
                        dictionaryToSave['hexCodes']['DEL'] = receiveSerial(ser, 'DEL')
                    elif event == 'SEARCH':
                        print('Pressed button SEARCH')
                        dictionaryToSave['hexCodes']['SEARCH'] = receiveSerial(ser, 'SEARCH')
                    elif event == 'UP':
                        print('Pressed button UP')
                        dictionaryToSave['hexCodes']['CHANNEL_UP'] = receiveSerial(ser, 'CHANNEL_UP')
                    elif event == 'DOWN':
                        print('Pressed button DOWN')
                        dictionaryToSave['hexCodes']['CHANNEL_DOWN'] = receiveSerial(ser, 'CHANNEL_DOWN')
                    elif event == 'RETURN':
                        print('Pressed button RETURN')
                        dictionaryToSave['hexCodes']['RETURN'] = receiveSerial(ser, 'RETURN')
                    elif event == 'EXIT':
                        print('Pressed button EXIT')
                        dictionaryToSave['hexCodes']['EXIT'] = receiveSerial(ser, 'EXIT')
                    elif event == 'ENTER':
                        print('Pressed button ENTER')
                        dictionaryToSave['hexCodes']['ENTER'] = receiveSerial(ser, 'ENTER')
                    elif event == '^':
                        print('Pressed button ^')
                        dictionaryToSave['hexCodes']['UP'] = receiveSerial(ser, 'UP')
                    elif event == '<':
                        print('Pressed button <')
                        dictionaryToSave['hexCodes']['LEFT'] = receiveSerial(ser, 'LEFT')
                    elif event == 'OK':
                        print('Pressed button OK')
                        dictionaryToSave['hexCodes']['OK_INFO'] = receiveSerial(ser, 'OK_INFO')
                    elif event == '>':
                        print('Pressed button >')
                        dictionaryToSave['hexCodes']['RIGHT'] = receiveSerial(ser, 'RIGHT')
                    elif event == 'v':
                        print('Pressed button v')
                        dictionaryToSave['hexCodes']['DOWN'] = receiveSerial(ser, 'DOWN')
                    elif event == 'A':
                        print('Pressed button RED')
                        dictionaryToSave['hexCodes']['RED'] = receiveSerial(ser, 'RED')
                    elif event == 'B':
                        print('Pressed button GREEN')
                        dictionaryToSave['hexCodes']['GREEN'] = receiveSerial(ser, 'GREEN')
                    elif event == 'C':
                        print('Pressed button YELLOW')
                        dictionaryToSave['hexCodes']['YELLOW'] = receiveSerial(ser, 'YELLOW')
                    elif event == 'D':
                        print('Pressed button BLUE')
                        dictionaryToSave['hexCodes']['BLUE'] = receiveSerial(ser, 'BLUE')
                    elif event == 'LANGUAGE':
                        print('Pressed button LANGUAGE')
                        dictionaryToSave['hexCodes']['LANGUAGE'] = receiveSerial(ser, 'LANGUAGE')
                    else:
                        print('Pressed button LIGAR/DESLIGAR')
                        dictionaryToSave['hexCodes']['ON_OFF'] = receiveSerial(ser, 'ON_OFF')
                    
                    #Refreshing Multiline box content
                    form['archive'].Update(pretty(dictionaryToSave))
                else:
                    sg.popup_ok('Não conectado1!', title='Erro')
            except:
                sg.popup_ok('Não conectado2!', title='Erro')

def main(dictionary):
    """Main window"""    

    # ------ Menu Definition ------ #      
    menu_def = [['File', ['Open', 'Read and Save...']],
            ['Help', ['Tutorial','About']], ] 

    form = sg.Window('Controle remoto IR',  element_justification='c', location=(500,100), icon=resource_path('mackenzie.ico'))
    bt = {'size':(5,1), 'font':('Franklin Gothic Book', 10), 'button_color':("black","#F8F8F8")}
    bt2 = {'size':(10,1), 'font':('Franklin Gothic Book', 8), 'button_color':("black","#F8F8F8")}
    bt3 = {'size':(12,1), 'font':('Franklin Gothic Book', 8), 'button_color':("black","#F8F8F8")}
    bt4 = {'size':(6,2), 'font':('Franklin Gothic Book', 8), 'button_color':("black","#F8F8F8")}
    ic = {'size':(8,1), 'font':('Franklin Gothic Book', 10)}
    btA = {'size':(5,1), 'font':('Franklin Gothic Book', 8)}

    layout = [
        [sg.Menu(menu_def, tearoff=True)],
        [sg.Text('  '), sg.Text('Porta serial', font=16), sg.Text('⬤', font=12, key='status', text_color='red')],
        [sg.InputCombo(values=COMS,key='porta', default_value=getName(dictionary, 'COM'), **ic),sg.InputCombo(values=BAUD,key='baud', default_value=getName(dictionary, 'baudrate'), **ic)],
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
    window = form.Layout(layout)

    while True:             # Event Loop
        event, values = window.read()
        
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
                form['status'].Update(text_color='green')
             except:
                form['status'].Update(text_color='red')
                sg.popup_ok('A comunicação não pôde ser estabelecida!', title='Erro')
        elif event == 'Open':
            loadedFile = sg.popup_get_file('Please enter a file name')
            try:
                with open(loadedFile) as file:
                    dictionary = yaml.load(file, Loader=yaml.FullLoader)
                    form['porta'].Update()
                    print(getName(dictionary, 'COM'))
                    if sg.popup_yes_no('Use this file as default?')=="Yes":
                        defaultFile['default_YAML'] = loadedFile
                        with open('default.yaml', 'w') as fp:
                            yaml.dump(defaultFile, fp)
            except:
                sg.popup_ok('Não foi possível abrir o arquivo!', title='Erro')
        elif event == 'Read and Save...':
            try:
                ser.close()
            except:
                pass
            readSave(dictionary)
        else: 
            try:
                if ser.isOpen():
                    form['status'].Update(text_color='green')
                    if event == 'DESCONECTAR':
                        try:
                            ser.close()
                            sg.popup_ok('Conexão fechada com sucesso!', title='Desconectado')
                            form['status'].Update(text_color='red')
                        except:
                            pass
                    elif event == 'HOME':
                        print('Pressed button HOME')
                        ser.write(stringFormatter(dictionary,'HOME').encode())
                    elif event == 'SOURCE':
                        print('Pressed button SOURCE')
                        ser.write(stringFormatter(dictionary,'SOURCE').encode())
                    elif event == 'MUTE':
                        print('Pressed button MUTE')
                        ser.write(stringFormatter(dictionary,'MUTE').encode())
                    elif event == 'SPACE':
                        print('Pressed button SPACE')
                        ser.write(stringFormatter(dictionary,'SPACE').encode())
                    elif event == '1':
                        print('Pressed button 1')
                        ser.write(stringFormatter(dictionary,'1').encode())
                    elif event == '2':
                        print('Pressed button 2')
                        ser.write(stringFormatter(dictionary,'2').encode())
                    elif event == '3':
                        print('Pressed button 3')
                        ser.write(stringFormatter(dictionary,'3').encode())
                    elif event == '4':
                        print('Pressed button 4')
                        ser.write(stringFormatter(dictionary,'4').encode())
                    elif event == '5':
                        print('Pressed button 5')
                        ser.write(stringFormatter(dictionary,'5').encode())
                    elif event == '6':
                        print('Pressed button 6')
                        ser.write(stringFormatter(dictionary,'6').encode())
                    elif event == '7':
                        print('Pressed button 7')
                        ser.write(stringFormatter(dictionary,'7').encode())
                    elif event == '8':
                        print('Pressed button 8')
                        ser.write(stringFormatter(dictionary,'8').encode())
                    elif event == '9':
                        print('Pressed button 9')
                        ser.write(stringFormatter(dictionary,'9').encode())
                    elif event == '0':
                        print('Pressed button 0')
                        ser.write(stringFormatter(dictionary,'0').encode())
                    elif event == '+':
                        print('Pressed button +')
                        ser.write(stringFormatter(dictionary,'+').encode())
                    elif event == '-':
                        print('Pressed button -')
                        ser.write(stringFormatter(dictionary,'-').encode())
                    elif event == 'DEL':
                        print('Pressed button DEL')
                        ser.write(stringFormatter(dictionary,'DEL').encode())
                    elif event == 'SEARCH':
                        print('Pressed button SEARCH')
                        ser.write(stringFormatter(dictionary,'SEARCH').encode())
                    elif event == 'UP':
                        print('Pressed button UP')
                        ser.write(stringFormatter(dictionary,'CHANNEL_UP').encode())
                    elif event == 'DOWN':
                        print('Pressed button DOWN')
                        ser.write(stringFormatter(dictionary,'CHANNEL_DOWN').encode())
                    elif event == 'RETURN':
                        print('Pressed button RETURN')
                        ser.write(stringFormatter(dictionary,'RETURN').encode())
                    elif event == 'EXIT':
                        print('Pressed button EXIT')
                        ser.write(stringFormatter(dictionary,'EXIT').encode())
                    elif event == 'ENTER':
                        print('Pressed button ENTER')
                        ser.write(stringFormatter(dictionary,'ENTER').encode())
                    elif event == '^':
                        print('Pressed button ^')
                        ser.write(stringFormatter(dictionary,'UP').encode())
                    elif event == '<':
                        print('Pressed button <')
                        ser.write(stringFormatter(dictionary,'LEFT').encode())
                    elif event == 'OK':
                        print('Pressed button OK')
                        ser.write(stringFormatter(dictionary,'OK_INFO').encode())
                    elif event == '>':
                        print('Pressed button >')
                        ser.write(stringFormatter(dictionary,'RIGHT').encode())
                    elif event == 'v':
                        print('Pressed button v')
                        ser.write(stringFormatter(dictionary,'DOWN').encode())
                    elif event == 'A':
                        print('Pressed button RED')
                        ser.write(stringFormatter(dictionary,'RED').encode())
                    elif event == 'B':
                        print('Pressed button GREEN')
                        ser.write(stringFormatter(dictionary,'GREEN').encode())
                    elif event == 'C':
                        print('Pressed button YELLOW')
                        ser.write(stringFormatter(dictionary,'YELLOW').encode())
                    elif event == 'D':
                        print('Pressed button BLUE')
                        ser.write(stringFormatter(dictionary,'BLUE').encode())
                    elif event == 'LANGUAGE':
                        print('Pressed button LANGUAGE')
                        ser.write(stringFormatter(dictionary,'LANGUAGE').encode())
                    else:
                        print('Pressed button LIGAR/DESLIGAR')
                        ser.write(stringFormatter(dictionary,'ON_OFF').encode())
                else:
                    sg.popup_ok('Não conectado!', title='Erro')
            except:
                sg.popup_ok('Não conectado!', title='Erro')
    form.close()


try:
    defaultFile = readYAML('default.yaml')
except:
    defaultFile['default_YAML'] = ""


# Try to read the default file, if it does not exist or the pointed YAML file does not exist, it loads some default hexcodes and writes to the default files
try:
    dictionary = readYAML(defaultFile['default_YAML'])
    print('Arquivo lido')
except:
    print('Arquivo não lido')
    dictionary = {'config': {'COM': 'COM 7', 'baudrate': 9600}, 'hexCodes': {'ON_OFF': '0xA1 0xF1 0x00 0xFF 0x1C', 'MUTE': '0xA1 0xF1 0x00 0xFF 0x08', 'HOME': '0xA1 0xF1 0x00 0xFF 0x08', 'MENU': '0xA1 0xF1 0x00 0xFF 0x49', 'Back': '0xA1 0xF1 0x00 0xFF 0x17', 'UP': '0xA1 0xF1 0x00 0xFF 0x1A', 'DOWN': '0xA1 0xF1 0x00 0xFF 0x48', 'RIGHT': '0xA1 0xF1 0x00 0xFF 0x07', 'LEFT': '0xA1 0xF1 0x00 0xFF 0x47', 'OK_INFO': '0xA1 0xF1 0x00 0xFF 0x06', 'ENTER': '0xA1 0xF1 0x00 0xFF 0x03', 'DEL': '0xA1 0xF1 0x00 0xFF 0x42', 'VOl_UP': '0xA1 0xF1 0x00 0xFF 0x4B', 'VOL_DOWN': '0xA1 0xF1 0x00 0xFF 0x4F', 'CHANNEL_UP': '0xA1 0xF1 0x00 0xFF 0x09', 'CHANNEL_DOWN': '0xA1 0xF1 0x00 0xFF 0x05', 1: '0xA1 0xF1 0x00 0xFF 0x54', 2: '0xA1 0xF1 0x00 0xFF 0x16', 3: '0xA1 0xF1 0x00 0xFF 0x15', 
    4: '0xA1 0xF1 0x00 0xFF 0x50', 5: '0xA1 0xF1 0x00 0xFF 0x12', 6: '0xA1 0xF1 0x00 0xFF 0x11', 7: '0xA1 0xF1 0x00 0xFF 0x4C', 8: '0xA1 0xF1 0x00 0xFF 0x0E', 9: '0xA1 0xF1 0x00 0xFF 0x0D', 0: '0xA1 0xF1 0x00 0xFF 0x0C', 'RED': '0xA1 0xF1 0x00 0xFF 0x01', 
    'GREEN': '0xA1 0xF1 0x00 0xFF 0x5F', 'BLUE': '0xA1 0xF1 0x00 0xFF 0x19', 'YELLOW': '0xA1 0xF1 0x00 0xFF 0x58', 'SPACE': '0xA1 0xF1 0x00 0xFF 0x10', 'LANGUAGE': '0xA1 0xF1 0x00 0xFF 0x41', 'SEARCH': '0xA1 0xF1 0x00 0xFF 0x0A'}}
    f = open('defaultControl.yaml', "w")
    with open('defaultControl.yaml', 'w') as file:
        documents = yaml.dump(dictionary, file)
    f.close()
    defaultFile['default_YAML'] = 'defaultControl.yaml'
    with open('default.yaml', 'w') as fp:
        yaml.dump(defaultFile, fp)

if __name__ == '__main__':
    main(dictionary)
