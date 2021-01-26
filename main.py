import GUI_all as gui
import DB_all as db

db.sozdanie()
choise = -1
while choise != 0:
    choise = gui.start_menu() 
        
    if choise == 1 or choise == 2:
        back_to_menu, values = gui.poisk(choise)
        if back_to_menu != 0 :
            arr = []
            for b in values.keys():
                if values[b] == '':
                    arr+= [b]
            for b in arr:
                del values[b]
            values = db.poisk(choise, values)
            values = gui.founded_objects(values)

    elif choise == 3 or choise == 4:
        back_to_menu, values = gui.dobavlenie(choise) 
        if back_to_menu != 0:
            db.dobavlenie(choise, values)    
    elif choise == 5:
        choise, values = gui.giving()
        if choise!=0:
            db.giving(values)
    elif choise == 6:
        choise, values = gui.geting()
        if choise!=0:
            db.geting(values)

