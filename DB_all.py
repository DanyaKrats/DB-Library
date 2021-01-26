import sqlite3 as sq
import fine
import GUI_all as gui
import datetime
def sozdanie():
    with sq.connect("Biblioteka.db") as con:
        #print("хей")
        cur = con.cursor()

       # cur.execute("DROP TABLE IF EXISTS books")
        #cur.execute("DROP TABLE IF EXISTS readers")
        cur.execute("""CREATE TABLE IF NOT EXISTS books (
            fond_number INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            autor TEXT NOT NULL,
            date,
            place,
            UDK,
            BBK,
            where_it_is
            )""")
        

        cur.execute("""CREATE TABLE IF NOT EXISTS readers (
            pasport PRIMARY KEY,
            firstname TEXT NOT NULL,
            secondname TEXT NOT NULL,
            book,
            date_of_taking_book
            )""")
    #print("DB done")
    cur.close()
    
def dobavlenie(choise, val):
    with sq.connect("Biblioteka.db") as con:
        cur = con.cursor()
        table = """readers"""
        if choise == 3:
            table = """books"""
    
        columns = ', '.join(val.keys())
        placeholders = ':'+', :'.join(val.keys())
        x = gui.cheking_corrtct(val)

        query = 'INSERT INTO '+ table +' (%s) VALUES (%s)' % (columns, placeholders)
        if x != 0:
            cur.execute(query, val)
        con.commit()  
    cur.close()  

def poisk(choise, val):
    with sq.connect("Biblioteka.db") as con:
        cur = con.cursor()
        table = """readers"""
        if choise == 1:
            table = """books"""
        columns = ', '.join(val.keys())
        placeholders = ':'+', :'.join(val.keys())
        query = 'SELECT * FROM '+ table +' WHERE  (%s) == (%s)' % (columns, placeholders)
        cur.execute(query, val)
        records = cur.fetchall()
        con.commit()  
    cur.close()
    return records

def giving(val):
    with sq.connect("Biblioteka.db") as con:
        print (val)
        cur = con.cursor()

        book = val["fond_number"]
        pasport = val["pasport"]

        print(book, pasport)

        c = {"pasport": val["pasport"]}
        print(c)
        check = poisk(2, c)
        print(check[0][0])
        if check[0][4]!= "0":
            gui.stop()
        else:
            print("nice")

            query ='UPDATE readers SET book = "' + book + '" WHERE pasport ==  "' + pasport + '"'
            cur.execute(query)
            query ='UPDATE readers SET date_of_taking_book = "'  + str(datetime.date.today()) + '" WHERE pasport ==  "' + pasport + '"'
            cur.execute(query)

            query ='UPDATE books SET where_it_is = "' + pasport + '" WHERE fond_number ==  "' + book + '"'
            cur.execute(query)

        con.commit()

    cur.close()
    return 0

def geting(val):
    with sq.connect("Biblioteka.db") as con:
        #print (val)
        cur = con.cursor()
        book ="1"
        
        pasport = val["pasport"]

        values = poisk(2,val)
        #print(values)
        if values[0][4] == "0":
            gui.stop2()
        else:
            book = values[0][3]
            #print(values[0][4])
            fines = fine.fine(values[0][4])
            if fines > 0:
                choise = gui.finegui(fines)
                if choise != 0:
                    query ='UPDATE books SET where_it_is = "В библиотеке" WHERE fond_number ==  "' + str(book) + '"'
                    cur.execute(query)
                    query ='UPDATE readers SET book = "0" WHERE pasport ==  "' + pasport + '"'
                    cur.execute(query)
                    query ='UPDATE readers SET date_of_taking_book = "0" WHERE pasport ==  "' + pasport + '"'
                    cur.execute(query)

        con.commit()

    cur.close()
    return 0
