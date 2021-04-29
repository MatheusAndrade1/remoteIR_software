import PySimpleGUI as sg
import platform
import serial
import os
import sys
import yaml
import time


image_icon = 'mackenzie.ico'
onoff = 'images\\on_off.png'
number1 = 'images\\number1.png'
number2 = 'images\\number2.png'
number3 = 'images\\number3.png'
number4 = 'images\\number4.png'
number5 = 'images\\number5.png'
number6 = 'images\\number6.png'
number7 = 'images\\number7.png'
number8 = 'images\\number8.png'
number9 = 'images\\number9.png'
number0 = 'images\\number0.png'
source = 'images\\source.png'
language = 'images\\language.png'
space = 'images\\space.png'
delete = 'images\\del.png'
enter = 'images\\enter.png'
volup = 'images\\volup.png'
voldown = 'images\\voldown.png'
chup = 'images\\chup.png'
chdown = 'images\\chdown.png'
mute = 'images\\mute.png'
exit = 'images\\exit.png'
returnButton = 'images\\return.png'
ok = 'images\\ok.png'
up = 'images\\up.png'
down = 'images\\down.png'
left = 'images\\left.png'
right = 'images\\right.png'
red = 'images\\red.png'
green = 'images\\green.png'
yellow = 'images\\yellow.png'
blue = 'images\\blue.png'
home = 'images\\home.png'
info = 'images\\info.png'
empty = 'images\\empty.png'
menu = 'images\\menu.png'
connect = 'images\\connect.png'
disconnect = 'images\\disconnect.png'


sg.ChangeLookAndFeel('SystemDefault1')

""" GLOBAL VARIABLES """
BAUD = ["9600", "19200", "57600", "115200"]

if platform.system().upper() == "WINDOWS":
    COMS = ["COM1", "COM2", "COM3", "COM4", "COM5", "COM6", "COM7", "COM8", "COM9"]
else:
    COMS = ["/dev/ttyUSB0", "/dev/ttyUSB1", "/dev/ttyUSB2", "/dev/ttyUSB3", "/dev/ttyUSB4", "/dev/ttyUSB5", "/dev/ttyUSB6", "/dev/ttyUSB7"]

defaultFile = {}


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

def getName(dictionary, item):
    """Load config options from the dictionary"""
    if dictionary['config'][item] is None:
        if item=='COM':
            return 'COM7'
        else:
            return '9600'
    else:
        if item=='COM':
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

def receiveSerial(ser, item):
    """Receive serial value, convert it to string and format"""
    ser.flushInput()
    time.sleep(.1)
    bytes_ = ser.read_until() # Receive until it finds '\n' by default
    text = str(bytes_)
    text = text.replace('\'','')
    text = text.replace('b','')
    return text.replace('\\n','')

   
def readSave(dictionaryToSave):
    """Form to load hexcodes and save them as YAML files"""
    # ------ Menu Definition ------ #      
    menu_def = [['File',['Save']]
    ] 
   
    form = sg.Window('Controle remoto IR',  element_justification='c', icon=resource_path('mackenzie.ico'))
    ic = {'size':(8,1), 'font':('Franklin Gothic Book', 10)}

    columnLeft = [
        [sg.Text(' '  * 16), sg.Text('Status', font=12), sg.Text('⬤', font=12, key='status', text_color='red')],
        [sg.Text(' '  * 4), sg.InputCombo(values=COMS,key='port', default_value=getName(dictionaryToSave, 'COM'), **ic),sg.InputCombo(values=BAUD,key='baud', default_value=getName(dictionaryToSave, 'baudrate'), **ic)],
        [sg.Text(' '  * 8), sg.Button(key='CONNECT', button_color=(sg.theme_background_color()), image_filename=resource_path(connect), image_subsample=1, border_width=0),sg.Button(key='DISCONNECT', button_color=(sg.theme_background_color()), image_filename=resource_path(disconnect), image_subsample=1, border_width=0)],
        [sg.Text('_'  * 32)],
        [sg.Button(button_color=(sg.theme_background_color()), image_filename=resource_path(onoff), image_subsample=1, border_width=0),sg.Button(key='1', button_color=(sg.theme_background_color()), image_filename=resource_path(number1), image_subsample=1, border_width=0),sg.Button(key='2', button_color=(sg.theme_background_color()), image_filename=resource_path(number2), image_subsample=1, border_width=0),sg.Button(key='3', button_color=(sg.theme_background_color()), image_filename=resource_path(number3), image_subsample=1, border_width=0)],
        [sg.Button(key='SOURCE', button_color=(sg.theme_background_color()), image_filename=resource_path(source), image_subsample=1, border_width=0),sg.Button(key='4', button_color=(sg.theme_background_color()), image_filename=resource_path(number4), image_subsample=1, border_width=0),sg.Button(key='5', button_color=(sg.theme_background_color()), image_filename=resource_path(number5), image_subsample=1, border_width=0),sg.Button(key='6', button_color=(sg.theme_background_color()), image_filename=resource_path(number6), image_subsample=1, border_width=0)],
        [sg.Button(key='LANGUAGE', button_color=(sg.theme_background_color()), image_filename=resource_path(language), image_subsample=1, border_width=0),sg.Button(key='7', button_color=(sg.theme_background_color()), image_filename=resource_path(number7), image_subsample=1, border_width=0),sg.Button(key='8', button_color=(sg.theme_background_color()), image_filename=resource_path(number8), image_subsample=1, border_width=0),sg.Button(key='9', button_color=(sg.theme_background_color()), image_filename=resource_path(number9), image_subsample=1, border_width=0)],
        [sg.Button(key='SPACE', button_color=(sg.theme_background_color()), image_filename=resource_path(space), image_subsample=1, border_width=0),sg.Button(key='DEL', button_color=(sg.theme_background_color()), image_filename=resource_path(delete), image_subsample=1, border_width=0),sg.Button(key='0', button_color=(sg.theme_background_color()), image_filename=resource_path(number0), image_subsample=1, border_width=0),sg.Button(key='ENTER', button_color=(sg.theme_background_color()), image_filename=resource_path(enter), image_subsample=1, border_width=0)],
        [sg.Button(key='VOLUP', button_color=(sg.theme_background_color()), image_filename=resource_path(volup), image_subsample=1, border_width=0),sg.Button(key='CHUP', button_color=(sg.theme_background_color()), image_filename=resource_path(chup), image_subsample=1, border_width=0),sg.Button(key='UP', button_color=(sg.theme_background_color()), image_filename=resource_path(up), image_subsample=1, border_width=0),sg.Button(key='EXIT', button_color=(sg.theme_background_color()), image_filename=resource_path(exit), image_subsample=1, border_width=0)],
        [sg.Button(key='MUTE', button_color=(sg.theme_background_color()), image_filename=resource_path(mute), image_subsample=1, border_width=0),sg.Button(key='LEFT', button_color=(sg.theme_background_color()), image_filename=resource_path(left), image_subsample=1, border_width=0),sg.Button(key='OK', button_color=(sg.theme_background_color()), image_filename=resource_path(ok), image_subsample=1, border_width=0),sg.Button(key='RIGHT', button_color=(sg.theme_background_color()), image_filename=resource_path(right), image_subsample=1, border_width=0)],
        [sg.Button(key='VOLDOWN', button_color=(sg.theme_background_color()), image_filename=resource_path(voldown), image_subsample=1, border_width=0),sg.Button(key='CHDOWN', button_color=(sg.theme_background_color()), image_filename=resource_path(chdown), image_subsample=1, border_width=0),sg.Button(key='DOWN', button_color=(sg.theme_background_color()), image_filename=resource_path(down), image_subsample=1, border_width=0),sg.Button(key='RETURN', button_color=(sg.theme_background_color()), image_filename=resource_path(returnButton), image_subsample=1, border_width=0)],
        [sg.Button(key='MENU', button_color=(sg.theme_background_color()), image_filename=resource_path(menu), image_subsample=1, border_width=0),sg.Button(key='HOME', button_color=(sg.theme_background_color()), image_filename=resource_path(home), image_subsample=1, border_width=0),sg.Button(key='INFO', button_color=(sg.theme_background_color()), image_filename=resource_path(info), image_subsample=1, border_width=0),sg.Button(key='EMPTY', button_color=(sg.theme_background_color()), image_filename=resource_path(empty), image_subsample=1, border_width=0)],
        [sg.Button(key='RED', button_color=(sg.theme_background_color()), image_filename=resource_path(red), image_subsample=1, border_width=0),sg.Button(key='GREEN', button_color=(sg.theme_background_color()), image_filename=resource_path(green), image_subsample=1, border_width=0),sg.Button(key='YELLOW', button_color=(sg.theme_background_color()), image_filename=resource_path(yellow), image_subsample=1, border_width=0),sg.Button(key='BLUE', button_color=(sg.theme_background_color()), image_filename=resource_path(blue), image_subsample=1, border_width=0)]
    ]

    columnRight = [
        [sg.Text('Configuration file: ', font=14)],
        [sg.Multiline(pretty(dictionaryToSave), size=(50, 30), font='4', background_color='white', text_color='black', key='archive')]
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
        if event == 'CONNECT':
             try:
                ser = serial.Serial(values['port'], values['baud'])
                sg.popup_ok('Communication established!', title='Success')
                form['status'].Update(text_color='green')
             except:
                form['status'].Update(text_color='red')
                sg.popup_ok('Communication cannot be established!', title='Error')
        elif event == 'Save':
            dictionaryToSave['config']['COM'] = values['port']
            dictionaryToSave['config']['baudrate'] = values['baud']
            path = sg.popup_get_file('Please enter a file name', save_as=True, default_extension='.yaml', file_types=(('YAML file', '.yaml'),))
            if path is not None:
                f = open(path, "w")
                with open(path, 'w') as file:
                    documents = yaml.dump(dictionaryToSave, file)
                f.close()
                if sg.popup_yes_no('Do you want to make this file default?')=='Yes':
                    defaultFile['default_YAML'] = path
                    with open('default.yaml', 'w') as fp:
                        yaml.dump(defaultFile, fp)
        else: 
            try:
                if ser.isOpen():
                    form['status'].Update(text_color='green')
                    if event == 'DISCONNECT':
                        try:
                            ser.close()
                            sg.popup_ok('Closed serial port!', title='Disconnected')
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
                    elif event == 'VOLUP':
                        print('Pressed button VOLUME UP')
                        dictionaryToSave['hexCodes']['+'] = receiveSerial(ser, '+')
                    elif event == 'VOLDOWN':
                        print('Pressed button VOLUME DOWN')
                        dictionaryToSave['hexCodes']['-'] = receiveSerial(ser, '-')
                    elif event == 'DEL':
                        print('Pressed button DEL')
                        dictionaryToSave['hexCodes']['DEL'] = receiveSerial(ser, 'DEL')
                    elif event == 'SEARCH':
                        print('Pressed button SEARCH')
                        dictionaryToSave['hexCodes']['SEARCH'] = receiveSerial(ser, 'SEARCH')
                    elif event == 'CHUP':
                        print('Pressed button CHANNEL UP')
                        dictionaryToSave['hexCodes']['CHANNEL_UP'] = receiveSerial(ser, 'CHANNEL_UP')
                    elif event == 'CHDOWN':
                        print('Pressed button CHANNEL DOWN')
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
                    elif event == 'UP':
                        print('Pressed button UP')
                        dictionaryToSave['hexCodes']['UP'] = receiveSerial(ser, 'UP')
                    elif event == 'LEFT':
                        print('Pressed button LEFT')
                        dictionaryToSave['hexCodes']['LEFT'] = receiveSerial(ser, 'LEFT')
                    elif event == 'OK':
                        print('Pressed button OK')
                        dictionaryToSave['hexCodes']['OK'] = receiveSerial(ser, 'OK')
                    elif event == 'RIGHT':
                        print('Pressed button RIGHT')
                        dictionaryToSave['hexCodes']['RIGHT'] = receiveSerial(ser, 'RIGHT')
                    elif event == 'DOWN':
                        print('Pressed button DOWN')
                        dictionaryToSave['hexCodes']['DOWN'] = receiveSerial(ser, 'DOWN')
                    elif event == 'RED':
                        print('Pressed button RED')
                        dictionaryToSave['hexCodes']['RED'] = receiveSerial(ser, 'RED')
                    elif event == 'GREEN':
                        print('Pressed button GREEN')
                        dictionaryToSave['hexCodes']['GREEN'] = receiveSerial(ser, 'GREEN')
                    elif event == 'YELLOW':
                        print('Pressed button YELLOW')
                        dictionaryToSave['hexCodes']['YELLOW'] = receiveSerial(ser, 'YELLOW')
                    elif event == 'BLUE':
                        print('Pressed button BLUE')
                        dictionaryToSave['hexCodes']['BLUE'] = receiveSerial(ser, 'BLUE')
                    elif event == 'LANGUAGE':
                        print('Pressed button LANGUAGE')
                        dictionaryToSave['hexCodes']['LANGUAGE'] = receiveSerial(ser, 'LANGUAGE')
                    elif event == 'HOME':
                        print('Pressed button HOME')
                        dictionaryToSave['hexCodes']['HOME'] = receiveSerial(ser, 'HOME')
                    elif event == 'INFO':
                        print('Pressed button INFO')
                        dictionaryToSave['hexCodes']['INFO'] = receiveSerial(ser, 'INFO')
                    elif event == 'MENU':
                        print('Pressed button MENU')
                        dictionaryToSave['hexCodes']['MENU'] = receiveSerial(ser, 'MENU')
                    elif event == 'EMPTY':
                        print('Pressed button EMPTY')
                    else:
                        print('Pressed button ON/OFF')
                        dictionaryToSave['hexCodes']['ON_OFF'] = receiveSerial(ser, 'ON_OFF')
                    
                    #Refreshing Multiline box content
                    form['archive'].Update(pretty(dictionaryToSave))
                else:
                    form['status'].Update(text_color='red')
                    sg.popup_ok('Disconnected!', title='Error')
            except:
                sg.popup_ok('Disconnected!', title='Error')

def main(dictionary):
    """Main window"""    
    # ------ Menu Definition ------ #      
    menu_def = [['File', ['Open', 'Read and Save...']],
            ['Help', ['Tutorial']], ] 

    
    form = sg.Window('Controle remoto IR',  element_justification='c', icon=resource_path('mackenzie.ico'))
    #bt = {'size':(12,1), 'font':('Franklin Gothic Book', 10), 'button_color':("black","#F8F8F8")}
    ic = {'size':(8,1), 'font':('Franklin Gothic Book', 10)}

    column1 = [
        [sg.Text(' '  * 16), sg.Text('Status', font=12), sg.Text('⬤', font=12, key='status', text_color='red')],
        [sg.Text(' '  * 4), sg.InputCombo(values=COMS,key='port', default_value=getName(dictionary, 'COM'), **ic),sg.InputCombo(values=BAUD,key='baud', default_value=getName(dictionary, 'baudrate'), **ic)],
        #[sg.Text(' '  * 17), sg.Button(button_text='CONNECT', **bt),sg.Button(button_text='DISCONNECT', **bt)],
        [sg.Text(' '  * 8), sg.Button(key='CONNECT', button_color=(sg.theme_background_color()), image_filename=resource_path(connect), image_subsample=1, border_width=0),sg.Button(key='DISCONNECT', button_color=(sg.theme_background_color()), image_filename=resource_path(disconnect), image_subsample=1, border_width=0)],
        [sg.Text('_'  * 32)],
        [sg.Button(button_color=(sg.theme_background_color()), image_filename=resource_path(onoff), image_subsample=1, border_width=0),sg.Button(key='1', button_color=(sg.theme_background_color()), image_filename=resource_path(number1), image_subsample=1, border_width=0),sg.Button(key='2', button_color=(sg.theme_background_color()), image_filename=resource_path(number2), image_subsample=1, border_width=0),sg.Button(key='3', button_color=(sg.theme_background_color()), image_filename=resource_path(number3), image_subsample=1, border_width=0)],
        [sg.Button(key='SOURCE', button_color=(sg.theme_background_color()), image_filename=resource_path(source), image_subsample=1, border_width=0),sg.Button(key='4', button_color=(sg.theme_background_color()), image_filename=resource_path(number4), image_subsample=1, border_width=0),sg.Button(key='5', button_color=(sg.theme_background_color()), image_filename=resource_path(number5), image_subsample=1, border_width=0),sg.Button(key='6', button_color=(sg.theme_background_color()), image_filename=resource_path(number6), image_subsample=1, border_width=0)],
        [sg.Button(key='LANGUAGE', button_color=(sg.theme_background_color()), image_filename=resource_path(language), image_subsample=1, border_width=0),sg.Button(key='7', button_color=(sg.theme_background_color()), image_filename=resource_path(number7), image_subsample=1, border_width=0),sg.Button(key='8', button_color=(sg.theme_background_color()), image_filename=resource_path(number8), image_subsample=1, border_width=0),sg.Button(key='9', button_color=(sg.theme_background_color()), image_filename=resource_path(number9), image_subsample=1, border_width=0)],
        [sg.Button(key='SPACE', button_color=(sg.theme_background_color()), image_filename=resource_path(space), image_subsample=1, border_width=0),sg.Button(key='DEL', button_color=(sg.theme_background_color()), image_filename=resource_path(delete), image_subsample=1, border_width=0),sg.Button(key='0', button_color=(sg.theme_background_color()), image_filename=resource_path(number0), image_subsample=1, border_width=0),sg.Button(key='ENTER', button_color=(sg.theme_background_color()), image_filename=resource_path(enter), image_subsample=1, border_width=0)],
        [sg.Button(key='VOLUP', button_color=(sg.theme_background_color()), image_filename=resource_path(volup), image_subsample=1, border_width=0),sg.Button(key='CHUP', button_color=(sg.theme_background_color()), image_filename=resource_path(chup), image_subsample=1, border_width=0),sg.Button(key='UP', button_color=(sg.theme_background_color()), image_filename=resource_path(up), image_subsample=1, border_width=0),sg.Button(key='EXIT', button_color=(sg.theme_background_color()), image_filename=resource_path(exit), image_subsample=1, border_width=0)],
        [sg.Button(key='MUTE', button_color=(sg.theme_background_color()), image_filename=resource_path(mute), image_subsample=1, border_width=0),sg.Button(key='LEFT', button_color=(sg.theme_background_color()), image_filename=resource_path(left), image_subsample=1, border_width=0),sg.Button(key='OK', button_color=(sg.theme_background_color()), image_filename=resource_path(ok), image_subsample=1, border_width=0),sg.Button(key='RIGHT', button_color=(sg.theme_background_color()), image_filename=resource_path(right), image_subsample=1, border_width=0)],
        [sg.Button(key='VOLDOWN', button_color=(sg.theme_background_color()), image_filename=resource_path(voldown), image_subsample=1, border_width=0),sg.Button(key='CHDOWN', button_color=(sg.theme_background_color()), image_filename=resource_path(chdown), image_subsample=1, border_width=0),sg.Button(key='DOWN', button_color=(sg.theme_background_color()), image_filename=resource_path(down), image_subsample=1, border_width=0),sg.Button(key='RETURN', button_color=(sg.theme_background_color()), image_filename=resource_path(returnButton), image_subsample=1, border_width=0)],
        [sg.Button(key='MENU', button_color=(sg.theme_background_color()), image_filename=resource_path(menu), image_subsample=1, border_width=0),sg.Button(key='HOME', button_color=(sg.theme_background_color()), image_filename=resource_path(home), image_subsample=1, border_width=0),sg.Button(key='INFO', button_color=(sg.theme_background_color()), image_filename=resource_path(info), image_subsample=1, border_width=0),sg.Button(key='EMPTY', button_color=(sg.theme_background_color()), image_filename=resource_path(empty), image_subsample=1, border_width=0)],
        [sg.Button(key='RED', button_color=(sg.theme_background_color()), image_filename=resource_path(red), image_subsample=1, border_width=0),sg.Button(key='GREEN', button_color=(sg.theme_background_color()), image_filename=resource_path(green), image_subsample=1, border_width=0),sg.Button(key='YELLOW', button_color=(sg.theme_background_color()), image_filename=resource_path(yellow), image_subsample=1, border_width=0),sg.Button(key='BLUE', button_color=(sg.theme_background_color()), image_filename=resource_path(blue), image_subsample=1, border_width=0)]
    ]

    layout = [
        [sg.Menu(menu_def, tearoff=True)],
        [sg.Column(column1, justification='center', vertical_alignment='center')]
    ]
    window = form.Layout(layout)

    while True:             # Event Loop
        event, values = window.read()

        codeToSend=""

        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Go':
            form['-OUT-'].update(values['-IN-'])

        #Botões
        if event == 'CONNECT':
             try:
                ser = serial.Serial(values['port'], values['baud'])
                ser.isOpen()
                sg.popup_ok('Communication established!', title='Success')
                form['status'].Update(text_color='green')
             except:
                form['status'].Update(text_color='red')
                sg.popup_ok('Communication cannot be established!', title='Error')
        elif event == 'Open':
            loadedFile = sg.popup_get_file('Please enter a file name')
            if loadedFile is not None:
                try:
                    with open(loadedFile) as file:
                        print(yaml.load(file, Loader=yaml.FullLoader))
                        if 'hexCodes' in readYAML(loadedFile):
                            dictionary = readYAML(loadedFile)
                            form['port'].Update()
                            if sg.popup_yes_no('Do you want to make this file default?')=="Yes":
                                defaultFile['default_YAML'] = loadedFile
                                with open('default.yaml', 'w') as fp:
                                    yaml.dump(defaultFile, fp)
                        else:
                            sg.popup_ok('Check file content!', title='Error')
                except:
                    sg.popup_ok('Cannot open the file!', title='Error')
        elif event == 'Read and Save...':
            try:
                ser.close()
                form['status'].Update(text_color='red')
            except:
                pass
            readSave(dictionary)
            form['port'].Update(dictionary['config']['COM'])
            form['baud'].Update(dictionary['config']['baudrate'])
        elif event=='Tutorial':
            sg.popup_ok('Not implemented yet!')
        else: 
            try:
                if ser.isOpen():
                    form['status'].Update(text_color='green')
                    if event == 'DISCONNECT':
                        try:
                            ser.close()
                            sg.popup_ok('Closed serial port!', title='Disconnected')
                            form['status'].Update(text_color='red')
                        except:
                            pass
                    elif event == 'HOME':
                        print('Pressed button HOME')
                        codeToSend = dictionary['hexCodes']['HOME'].split(" ")
                        print(codeToSend[3])
                        ser.write(serial.to_bytes([int(codeToSend[0], base=16), int(codeToSend[1], base=16), int(codeToSend[2], base=16), int(codeToSend[3], base=16), int(codeToSend[4], base=16)]))
                    elif event == 'SOURCE':
                        print('Pressed button SOURCE')
                        codeToSend = dictionary['hexCodes']['SOURCE'].split(" ")
                        ser.write(serial.to_bytes([int(codeToSend[0], base=16), int(codeToSend[1], base=16), int(codeToSend[2], base=16), int(codeToSend[3], base=16), int(codeToSend[4], base=16)]))
                    elif event == 'MUTE':
                        print('Pressed button MUTE')
                        codeToSend = dictionary['hexCodes']['MUTE'].split(" ")
                        ser.write(serial.to_bytes([int(codeToSend[0], base=16), int(codeToSend[1], base=16), int(codeToSend[2], base=16), int(codeToSend[3], base=16), int(codeToSend[4], base=16)]))
                    elif event == 'SPACE':
                        print('Pressed button SPACE')
                        codeToSend = dictionary['hexCodes']['SPACE'].split(" ")
                        ser.write(serial.to_bytes([int(codeToSend[0], base=16), int(codeToSend[1], base=16), int(codeToSend[2], base=16), int(codeToSend[3], base=16), int(codeToSend[4], base=16)]))
                    elif event == '1':
                        print('Pressed button 1')
                        codeToSend = dictionary['hexCodes']['1'].split(" ")
                        ser.write(serial.to_bytes([int(codeToSend[0], base=16), int(codeToSend[1], base=16), int(codeToSend[2], base=16), int(codeToSend[3], base=16), int(codeToSend[4], base=16)]))
                    elif event == '2':
                        print('Pressed button 2')
                        codeToSend = dictionary['hexCodes']['2'].split(" ")
                        ser.write(serial.to_bytes([int(codeToSend[0], base=16), int(codeToSend[1], base=16), int(codeToSend[2], base=16), int(codeToSend[3], base=16), int(codeToSend[4], base=16)]))
                    elif event == '3':
                        print('Pressed button 3')
                        codeToSend = dictionary['hexCodes']['3'].split(" ")
                        ser.write(serial.to_bytes([int(codeToSend[0], base=16), int(codeToSend[1], base=16), int(codeToSend[2], base=16), int(codeToSend[3], base=16), int(codeToSend[4], base=16)]))
                    elif event == '4':
                        print('Pressed button 4')
                        codeToSend = dictionary['hexCodes']['4'].split(" ")
                        ser.write(serial.to_bytes([int(codeToSend[0], base=16), int(codeToSend[1], base=16), int(codeToSend[2], base=16), int(codeToSend[3], base=16), int(codeToSend[4], base=16)]))
                    elif event == '5':
                        print('Pressed button 5')
                        codeToSend = dictionary['hexCodes']['5'].split(" ")
                        ser.write(serial.to_bytes([int(codeToSend[0], base=16), int(codeToSend[1], base=16), int(codeToSend[2], base=16), int(codeToSend[3], base=16), int(codeToSend[4], base=16)]))
                    elif event == '6':
                        print('Pressed button 6')
                        codeToSend = dictionary['hexCodes']['6'].split(" ")
                        ser.write(serial.to_bytes([int(codeToSend[0], base=16), int(codeToSend[1], base=16), int(codeToSend[2], base=16), int(codeToSend[3], base=16), int(codeToSend[4], base=16)]))
                    elif event == '7':
                        print('Pressed button 7')
                        codeToSend = dictionary['hexCodes']['7'].split(" ")
                        ser.write(serial.to_bytes([int(codeToSend[0], base=16), int(codeToSend[1], base=16), int(codeToSend[2], base=16), int(codeToSend[3], base=16), int(codeToSend[4], base=16)]))
                    elif event == '8':
                        print('Pressed button 8')
                        codeToSend = dictionary['hexCodes']['8'].split(" ")
                        ser.write(serial.to_bytes([int(codeToSend[0], base=16), int(codeToSend[1], base=16), int(codeToSend[2], base=16), int(codeToSend[3], base=16), int(codeToSend[4], base=16)]))
                    elif event == '9':
                        print('Pressed button 9')
                        codeToSend = dictionary['hexCodes']['9'].split(" ")
                        ser.write(serial.to_bytes([int(codeToSend[0], base=16), int(codeToSend[1], base=16), int(codeToSend[2], base=16), int(codeToSend[3], base=16), int(codeToSend[4], base=16)]))
                    elif event == '0':
                        print('Pressed button 0')
                        codeToSend = dictionary['hexCodes']['0'].split(" ")
                        ser.write(serial.to_bytes([int(codeToSend[0], base=16), int(codeToSend[1], base=16), int(codeToSend[2], base=16), int(codeToSend[3], base=16), int(codeToSend[4], base=16)]))
                    elif event == 'VOLUP':
                        print('Pressed button VOLUME UP')
                        codeToSend = dictionary['hexCodes']['+'].split(" ")
                        ser.write(serial.to_bytes([int(codeToSend[0], base=16), int(codeToSend[1], base=16), int(codeToSend[2], base=16), int(codeToSend[3], base=16), int(codeToSend[4], base=16)]))
                    elif event == 'VOLDOWN':
                        print('Pressed button VOLUME DOWN')
                        codeToSend = dictionary['hexCodes']['-'].split(" ")
                        ser.write(serial.to_bytes([int(codeToSend[0], base=16), int(codeToSend[1], base=16), int(codeToSend[2], base=16), int(codeToSend[3], base=16), int(codeToSend[4], base=16)]))
                    elif event == 'DEL':
                        print('Pressed button DEL')
                        codeToSend = dictionary['hexCodes']['DEL'].split(" ")
                        ser.write(serial.to_bytes([int(codeToSend[0], base=16), int(codeToSend[1], base=16), int(codeToSend[2], base=16), int(codeToSend[3], base=16), int(codeToSend[4], base=16)]))
                    elif event == 'SEARCH':
                        print('Pressed button SEARCH')
                        codeToSend = dictionary['hexCodes']['SEARCH'].split(" ")
                        ser.write(serial.to_bytes([int(codeToSend[0], base=16), int(codeToSend[1], base=16), int(codeToSend[2], base=16), int(codeToSend[3], base=16), int(codeToSend[4], base=16)]))
                    elif event == 'CHUP':
                        print('Pressed button CHANNEL UP')
                        codeToSend = dictionary['hexCodes']['CHANNEL_UP'].split(" ")
                        ser.write(serial.to_bytes([int(codeToSend[0], base=16), int(codeToSend[1], base=16), int(codeToSend[2], base=16), int(codeToSend[3], base=16), int(codeToSend[4], base=16)]))
                    elif event == 'CHDOWN':
                        print('Pressed button CHANNEL DOWN')
                        codeToSend = dictionary['hexCodes']['CHANNEL_DOWN'].split(" ")
                        ser.write(serial.to_bytes([int(codeToSend[0], base=16), int(codeToSend[1], base=16), int(codeToSend[2], base=16), int(codeToSend[3], base=16), int(codeToSend[4], base=16)]))
                    elif event == 'RETURN':
                        print('Pressed button RETURN')
                        codeToSend = dictionary['hexCodes']['RETURN'].split(" ")
                        ser.write(serial.to_bytes([int(codeToSend[0], base=16), int(codeToSend[1], base=16), int(codeToSend[2], base=16), int(codeToSend[3], base=16), int(codeToSend[4], base=16)]))
                    elif event == 'EXIT':
                        print('Pressed button EXIT')
                        codeToSend = dictionary['hexCodes']['EXIT'].split(" ")
                        ser.write(serial.to_bytes([int(codeToSend[0], base=16), int(codeToSend[1], base=16), int(codeToSend[2], base=16), int(codeToSend[3], base=16), int(codeToSend[4], base=16)]))
                    elif event == 'ENTER':
                        print('Pressed button ENTER')
                        codeToSend = dictionary['hexCodes']['ENTER'].split(" ")
                        ser.write(serial.to_bytes([int(codeToSend[0], base=16), int(codeToSend[1], base=16), int(codeToSend[2], base=16), int(codeToSend[3], base=16), int(codeToSend[4], base=16)]))
                    elif event == 'UP':
                        print('Pressed button UP')
                        codeToSend = dictionary['hexCodes']['UP'].split(" ")
                        ser.write(serial.to_bytes([int(codeToSend[0], base=16), int(codeToSend[1], base=16), int(codeToSend[2], base=16), int(codeToSend[3], base=16), int(codeToSend[4], base=16)]))
                    elif event == 'LEFT':
                        print('Pressed button LEFT')
                        codeToSend = dictionary['hexCodes']['LEFT'].split(" ")
                        ser.write(serial.to_bytes([int(codeToSend[0], base=16), int(codeToSend[1], base=16), int(codeToSend[2], base=16), int(codeToSend[3], base=16), int(codeToSend[4], base=16)]))
                    elif event == 'OK':
                        print('Pressed button OK')
                        codeToSend = dictionary['hexCodes']['OK'].split(" ")
                        ser.write(serial.to_bytes([int(codeToSend[0], base=16), int(codeToSend[1], base=16), int(codeToSend[2], base=16), int(codeToSend[3], base=16), int(codeToSend[4], base=16)]))
                    elif event == 'RIGHT':
                        print('Pressed button RIGHT')
                        codeToSend = dictionary['hexCodes']['RIGHT'].split(" ")
                        ser.write(serial.to_bytes([int(codeToSend[0], base=16), int(codeToSend[1], base=16), int(codeToSend[2], base=16), int(codeToSend[3], base=16), int(codeToSend[4], base=16)]))
                    elif event == 'DOWN':
                        print('Pressed button DOWN')
                        codeToSend = dictionary['hexCodes']['DOWN'].split(" ")
                        ser.write(serial.to_bytes([int(codeToSend[0], base=16), int(codeToSend[1], base=16), int(codeToSend[2], base=16), int(codeToSend[3], base=16), int(codeToSend[4], base=16)]))
                    elif event == 'RED':
                        print('Pressed button RED')
                        codeToSend = dictionary['hexCodes']['RED'].split(" ")
                        ser.write(serial.to_bytes([int(codeToSend[0], base=16), int(codeToSend[1], base=16), int(codeToSend[2], base=16), int(codeToSend[3], base=16), int(codeToSend[4], base=16)]))
                    elif event == 'GREEN':
                        print('Pressed button GREEN')
                        codeToSend = dictionary['hexCodes']['GREEN'].split(" ")
                        ser.write(serial.to_bytes([int(codeToSend[0], base=16), int(codeToSend[1], base=16), int(codeToSend[2], base=16), int(codeToSend[3], base=16), int(codeToSend[4], base=16)]))
                    elif event == 'YELLOW':
                        print('Pressed button YELLOW')
                        codeToSend = dictionary['hexCodes']['YELLOW'].split(" ")
                        ser.write(serial.to_bytes([int(codeToSend[0], base=16), int(codeToSend[1], base=16), int(codeToSend[2], base=16), int(codeToSend[3], base=16), int(codeToSend[4], base=16)]))
                    elif event == 'BLUE':
                        print('Pressed button BLUE')
                        codeToSend = dictionary['hexCodes']['BLUE'].split(" ")
                        ser.write(serial.to_bytes([int(codeToSend[0], base=16), int(codeToSend[1], base=16), int(codeToSend[2], base=16), int(codeToSend[3], base=16), int(codeToSend[4], base=16)]))
                    elif event == 'LANGUAGE':
                        print('Pressed button LANGUAGE')
                        codeToSend = dictionary['hexCodes']['LANGUAGE'].split(" ")
                        ser.write(serial.to_bytes([int(codeToSend[0], base=16), int(codeToSend[1], base=16), int(codeToSend[2], base=16), int(codeToSend[3], base=16), int(codeToSend[4], base=16)]))
                    elif event == 'HOME':
                        print('Pressed button HOME')
                        codeToSend = dictionary['hexCodes']['HOME'].split(" ")
                        ser.write(serial.to_bytes([int(codeToSend[0], base=16), int(codeToSend[1], base=16), int(codeToSend[2], base=16), int(codeToSend[3], base=16), int(codeToSend[4], base=16)]))
                    elif event == 'INFO':
                        print('Pressed button INFO')
                        codeToSend = dictionary['hexCodes']['INFO'].split(" ")
                        ser.write(serial.to_bytes([int(codeToSend[0], base=16), int(codeToSend[1], base=16), int(codeToSend[2], base=16), int(codeToSend[3], base=16), int(codeToSend[4], base=16)]))
                    elif event == 'MENU':
                        print('Pressed button MENU')
                        codeToSend = dictionary['hexCodes']['MENU'].split(" ")
                        ser.write(serial.to_bytes([int(codeToSend[0], base=16), int(codeToSend[1], base=16), int(codeToSend[2], base=16), int(codeToSend[3], base=16), int(codeToSend[4], base=16)]))
                    elif event == 'EMPTY':
                        print('Pressed button EMPTY')
                    else:
                        print('Pressed button ON/OFF')
                        codeToSend = dictionary['hexCodes']['ON_OFF'].split(" ")
                        ser.write(serial.to_bytes([int(codeToSend[0], base=16), int(codeToSend[1], base=16), int(codeToSend[2], base=16), int(codeToSend[3], base=16), int(codeToSend[4], base=16)]))
                else:
                    form['status'].Update(text_color='red')
                    sg.popup_ok('Disconnected!', title='Erro')
            except:
                sg.popup_ok('Disconnected!', title='Error')
    form.close()


"""Try to read the default file, if it does not exist or the pointed YAML file does not exist, it loads some default hexcodes and writes to the default files"""
try:
    defaultFile = readYAML('default.yaml')
except:
    defaultFile['default_YAML'] = ""
try:
    dictionary = readYAML(defaultFile['default_YAML'])
    print('Arquivo lido')
except:
    print('Arquivo não lido')
    dictionary = {'config': {'COM': 'COM7', 'baudrate': 9600}, 'hexCodes': {'ON_OFF': '0xA1 0xF1 0x00 0xFF 0x1C', 'MUTE': '0xA1 0xF1 0x00 0xFF 0x08', 'HOME': '0xA1 0xF1 0x00 0xFF 0x18', 'MENU': '0xA1 0xF1 0x00 0xFF 0x49', 'Back': '0xA1 0xF1 0x00 0xFF 0x17', 'UP': '0xA1 0xF1 0x00 0xFF 0x1A', 'DOWN': '0xA1 0xF1 0x00 0xFF 0x48', 'RIGHT': '0xA1 0xF1 0x00 0xFF 0x07', 'LEFT': '0xA1 0xF1 0x00 0xFF 0x47', 'OK': '0xA1 0xF1 0x00 0xFF 0x18', 'ENTER': '0xA1 0xF1 0x00 0xFF 0x03', 'DEL': '0xA1 0xF1 0x00 0xFF 0x42', 'VOl_UP': '0xA1 0xF1 0x00 0xFF 0x4B', 'VOL_DOWN': '0xA1 0xF1 0x00 0xFF 0x4F', 'CHANNEL_UP': '0xA1 0xF1 0x00 0xFF 0x09', 'CHANNEL_DOWN': '0xA1 0xF1 0x00 0xFF 0x05', 1: '0xA1 0xF1 0x00 0xFF 0x54', 2: '0xA1 0xF1 0x00 0xFF 0x16', 3: '0xA1 0xF1 0x00 0xFF 0x15', 
    4: '0xA1 0xF1 0x00 0xFF 0x50', 5: '0xA1 0xF1 0x00 0xFF 0x12', 6: '0xA1 0xF1 0x00 0xFF 0x11', 7: '0xA1 0xF1 0x00 0xFF 0x4C', 8: '0xA1 0xF1 0x00 0xFF 0x0E', 9: '0xA1 0xF1 0x00 0xFF 0x0D', 0: '0xA1 0xF1 0x00 0xFF 0x0C', 'RED': '0xA1 0xF1 0x00 0xFF 0x01', 
    'GREEN': '0xA1 0xF1 0x00 0xFF 0x5F', 'BLUE': '0xA1 0xF1 0x00 0xFF 0x19', 'YELLOW': '0xA1 0xF1 0x00 0xFF 0x58', 'SPACE': '0xA1 0xF1 0x00 0xFF 0x10', 'INFO': '0xA1 0xF1 0x00 0xFF 0x06', 'LANGUAGE': '0xA1 0xF1 0x00 0xFF 0x41', 'SEARCH': '0xA1 0xF1 0x00 0xFF 0x0A'}}
    f = open('defaultControl.yaml', "w")
    with open('defaultControl.yaml', 'w') as file:
        documents = yaml.dump(dictionary, file)
    f.close()
    defaultFile['default_YAML'] = 'defaultControl.yaml'
    with open('default.yaml', 'w') as fp:
        yaml.dump(defaultFile, fp)

if __name__ == '__main__':
    main(dictionary)
