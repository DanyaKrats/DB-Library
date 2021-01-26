import PySimpleGUI as sg
import datetime as dt
import fine


def cheking_corrtct(val):
    x = 1
    layout = []
    for elem in val:
        if val[elem] == "":  
            x = 0 
            layout = [
            [sg.Text("Вы заполнили не все поля!")], 
            [sg.Button('Выход')]
            ]
        else:
            layout = [
            [sg.Text("Добавление прошло успешно")], 
            [sg.Button('Выход')]
            ]
    window = sg.Window('БИБЛИОТЕКА', layout)
    while True :   
                event, values = window.read()
    #            print(values)
                if event == sg.WINDOW_CLOSED or event == 'Выход':
                    break
        
    window.close()
    return x

def start_menu():
    choise = -1
    layout = [
        [sg.Text("Добро пожаловать в Библиотеку")], 
        [sg.Text(" ")],
        [sg.Button('Выдать книгу', size = (20,0)), sg.Button('Вернуть книгу', size = (20,0))],
        [sg.Button('Найти книгу', size = (20,0)), sg.Button('Добавить книгу', size = (20,0))], 
        [sg.Button('Найти читателя', size = (20,0)), sg.Button('Добавить читателя', size = (20,0))],
        [sg.Button('Выход')]
    ]
    window = sg.Window('БИБЛИОТЕКА', layout)
    while choise == -1 :                             # The Event Loop
        event, values = window.read()
        if event == 'Выдать книгу':
            choise = 5
            break
        if event == 'Вернуть книгу':
            choise = 6
            break

        if event == 'Найти книгу':
            choise = 1
            break
        if event == 'Найти читателя':
            choise = 2
            break 
        if event == 'Добавить книгу':
            choise = 3
            break
        if event == 'Добавить читателя':
            choise = 4
            break 
        if event == sg.WINDOW_CLOSED or event == 'Выход':
            choise = 0
            break

    window.close()
    return choise

def poisk(choise):
    if choise == 1:
        layout = [
            [sg.Text("Поиск книги")], 
            [sg.Text(" ")],
            [sg.Text('Фондовый номер', size = (20,0)), sg.Input(key='fond_number')],
            [sg.Text('Название', size = (20,0)), sg.Input(key='name')],
            [sg.Text('Автор', size = (20,0)), sg.Input(key='autor')],
            [sg.Text('Дата выпуска', size = (20,0)), sg.Input(key='date')],
            [sg.Text('Место издания', size = (20,0)), sg.Input(key='place')],
            [sg.Text('Шифр УДК', size = (20,0)), sg.Input(key='UDK')],
            [sg.Text('Шифр ББК', size = (20,0)), sg.Input(key='BBK')],
            [sg.Text('В библиотке / Номер паспорта)', size = (20,0)), sg.Input(key='where_it_is')],
            [sg.Text(" ")],
            [sg.Button('Поиск'), sg.Button('Вернуться в меню')]
        ]
    if choise == 2:
        layout = [
            [sg.Text("Поиск читателя", size = (20,0))], 
            [sg.Text(" ")],
            [sg.Text('Паспорт', size = (20,0)), sg.Input(key='pasport')],
            [sg.Text('Имя', size = (20,0)), sg.Input(key='firstname')],
            [sg.Text('Фамилия', size = (20,0)), sg.Input(key='secondname')],
            [sg.Text('Фондовый номер книги', size = (20,0)), sg.Input(key='book')],
            [sg.Text(" ")],
            [sg.Button('Поиск'), sg.Button('Вернуться в меню')]
            ]
    back_to_menu = -1
    window = sg.Window('БИБЛИОТЕКА', layout)
    while True:
        event, values = window.read()
        if event == 'Поиск':
            back_to_menu = 1
            break
        if event == sg.WINDOW_CLOSED or event == 'Вернуться в меню':
            back_to_menu = 0
            break

    #print(event, values, back_to_menu) #debug
    window.close()
    return back_to_menu, values

def dobavlenie(choise):

    if choise == 3 :
        layout = [
            [sg.Text("Добавление книги")], 
            [sg.Text(" ")],
            [sg.Text('Фондовый номер', size = (20,0)), sg.Input(key='fond_number')],
            [sg.Text('Название', size = (20,0)), sg.Input(key='name')],
            [sg.Text('Автор', size = (20,0)), sg.Input(key='autor')],
            [sg.Text('Дата выпуска', size = (20,0)), sg.Input(key='date')],
            [sg.Text('Место издания', size = (20,0)), sg.Input(key='place')],
            [sg.Text('Шифр УДК', size = (20,0)), sg.Input(key='UDK')],
            [sg.Text('Шифр ББК', size = (20,0)), sg.Input(key='BBK')],
            [sg.Text(" ")],
            [sg.Button('Добавить', size = (20,0)), sg.Button('Вернуться в меню', size = (20,0))]
        ]
    if choise == 4:
            layout = [
            [sg.Text("Добавление читателя")], 
            [sg.Text(" ")],
            [sg.Text('Паспорт', size = (20,0)), sg.Input(key='pasport')],
            [sg.Text('Имя', size = (20,0)), sg.Input(key='firstname')],
            [sg.Text('Фамилия', size = (20,0)), sg.Input(key='secondname')],
            [sg.Text(" ")],
            [sg.Button('Добавить', size = (20,0)), sg.Button('Вернуться в меню', size = (20,0))]
        ]
   
    window = sg.Window('БИБЛИОТЕКА', layout)

    back_to_menu =-1

    while True:
        event, values = window.read()
        if event == 'Добавить':
            back_to_menu = 1
            break
        if event == sg.WINDOW_CLOSED or event == 'Вернуться в меню' or event == sg.WIN_CLOSED:
            back_to_menu = 0
            break
        
    window.close()

    if choise == 3:
        values['where_it_is'] = 'В библиотеке' 
    elif choise == 4:
        values["book"] = '0'
        values["date_of_taking_book"] = '0'


    return back_to_menu, values

def founded_objects(val):

    valstr = []
    for book in val:
         valstr += [str(book[0])+" | "+ book[1]+" | "+book[2]+" | " +  book[len(book)-1]]
    a = len(valstr)
 
    layout = [[sg.Text('Результаты поиска :'), sg.Button('Вернуться в меню')],
            *[[sg.Button(f'{i}')] for i in valstr]]
       
    window = sg.Window('БИБЛИОТЕКА', layout)
    cr = ''
    while True:
        event, values = window.read()

        if event == sg.WINDOW_CLOSED or event == 'Вернуться в меню' or event == sg.WIN_CLOSED:
             break
        else:
            cr = event
            break
    window.close()

    cr = cr[:cr.find("|")- 1]
    
    thatbook = 0
    
    for book in val:
        if str(book[0]) == str(cr):
            thatbook = book

    layout = [[sg.Text('Результаты поиска'), sg.Button("Вернуться в меню")],
    *[[sg.Text(f'{i}')] for i in thatbook]]

    window = sg.Window('БИБЛИОТЕКА', layout)

    while True:
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Вернуться в меню' or event == sg.WIN_CLOSED:
             break
        
    window.close()  
    return values

def information_about(choise, values):

    layout = [[sg.Text('Результаты поиска :')],
            *[[sg.Button(f'{i}')] for i in values],
              [sg.Button("Выход")]] 

    window = sg.Window('Ошибка', layout)
    while True :   
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Выход':
            break
        
    window.close()
    return values

def giving():
    choise = -1
    layout = [
        [sg.Text("Паспортные данные читателя", size = (20,0)), sg.Input(key='pasport') ], 
        [sg.Text("Фондовый номер книги", size = (20,0)), sg.Input(key='fond_number')],
        [sg.Button('Ввести'), sg.Button('Выход')]
    ]


    window = sg.Window('БИБЛИОТЕКА', layout)
    while True :   
        event, values = window.read()         
        if event == 'Ввести':     
            break            
        if event == sg.WINDOW_CLOSED or event == 'Выход':
            choise = 0
            break
    
    window.close()
    return choise, values

def geting():
    choise = -1
    layout = [
        [sg.Text("Паспортные данные читателя", size = (20,0)), sg.Input(key='pasport') ], 
        [sg.Button('Ввести', size = (20,0)), sg.Button('Выход', size = (20,0))]
    ]


    window = sg.Window('БИБЛИОТЕКА', layout)
    while True :   
        event, values = window.read()         
        if event == 'Ввести':     
            break            
        if event == sg.WINDOW_CLOSED or event == 'Выход':
            choise = 0
            break
        
    window.close()
    return choise, values

def finegui(fine):   
    layout = [
        [sg.Text("Штраф за просрочку : " + str(fine) + " рублей!")], 
        [sg.Button('Оплата', size = (20,0)), sg.Button('Выход', size = (20,0))]
    ]
    window = sg.Window('БИБЛИОТЕКА', layout)
    while True :   
        event, values = window.read()         
        if event == 'Оплата':     
            choise = -1
            break            
        if event == sg.WINDOW_CLOSED or event == 'Выход':
            choise = 0
            break
        
    window.close()
    return choise, values

def stop():   
    layout = [
        [sg.Text("Вы не вернули книгу!")], 
        [sg.Button('Выход')]
    ]


    window = sg.Window('Ошибка', layout)
    while True :   
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Выход':
            break
        
    window.close()
    return values

def stop2():   
    layout = [
        [sg.Text("На вас не записана книга!")], 
        [sg.Button('Выход')]
    ]


    window = sg.Window('Ошибка', layout)
    while True :   
        event, values = window.read()
        if event == sg.WINDOW_CLOSED or event == 'Выход':
            break
        
    window.close()
    return values


    