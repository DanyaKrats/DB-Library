import datetime

def fine(b):
    print(b)
    if b == None:
        return 0
    a = str(datetime.date.today())
    a = a.split('-')
    b = b.split('-')
    aa = datetime.date(int(a[0]),int(a[1]),int(a[2]))
    bb = datetime.date(int(b[0]),int(b[1]),int(b[2]))
    cc = aa-bb
    dd = str(cc)
    fine1 = (int(dd.split()[0]) - 14)*10
    return  fine1

fine("1999-12-12")


