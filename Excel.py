import xlrd, xlwt
import DB_all as db

def vigruzkab():
    rb = xlrd.open_workbook('Библиотека.xlsx')
    sheet = rb.sheet_by_index(0)
    vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
    
    values = {}
    
    if True == True:
        for  myList2 in vals:
             values.clear()
             #print("########################################")
             values['fond_number'] = str(myList2[0])
             values['name']= str(myList2[1])
             values['autor'] = str(myList2[2] )
             values['date'] = str(myList2[3]) 
             values['place'] = str(myList2[4])
             values['UDK'] = str(myList2[5] )
             values['BBK'] = str(myList2[6] )
             values['where_it_is'] = str(myList2[7] )
             
             print (values)
             db.dobavlenie(3, values) 
    
    return(values)

def vigruzkar():
    rb = xlrd.open_workbook('Читатели.xlsx')
    sheet = rb.sheet_by_index(0)
    vals = [sheet.row_values(rownum) for rownum in range(sheet.nrows)]
    
    values = {}
    
    if True == True:
        for  myList2 in vals:
             values.clear()
             #print("########################################")
             values['pasport'] = str(myList2[0])
             values['firstname']= str(myList2[1])
             values['secondname'] = str(myList2[2] )
             values['book'] = str(myList2[3]) 
             values['date_of_taking_book'] = str(myList2[4])
             print (values)
             db.dobavlenie(4, values) 
    
    return(values)

values = vigruzkar()
values = vigruzkab()
#print(values)