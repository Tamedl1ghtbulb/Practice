def main():
    while True:
        try:
            l= input('Fraction: ')
            try:
                t = l.index("/") #najlaksi nacin ya unos bilo cega osim / buduci da dole vec imamo ispistan exeption za ValueError
            except:
                continue
            a = l.split("/")
            x = a[0]
            y = a[1]
            if x.find(".")!= -1 or x.find(",")!=-1:
                continue
            y = a[1]
            if y.find(".")!= -1 or y.find(",")!=-1:
                continue
            try:
                x, y = int(x), int(y)
            except:
                continue
#            if y == 0:
#                print('neispravan unos, ispravan unos je "X/Y", bez nula u imeniocu, pri cemu je x vece od y probajte ponovo.')
#                raise ValueError
#                continue
            if x>y:
#                print('neispravan unos, ispravan unos je "X/Y", bez nula u imeniocu, pri cemu je x vece od y probajte ponovo.')
#                raise ValueError
                continue
            else:
                q= x/y
        except ValueError and ZeroDivisionError:
             print('neispravan unos, ispravan unos je "X/Y", bey nula u imeniocu, probajte ponovo.')
             continue
        k = convert(l)
        gauge(k)
        break
def convert(a):
    l = a.index("/") #nacin za unos / buduci da dole vec imamo ispistan exception za ValueError
    a = a.split("/")
    x = a[0]
    y = a[1]
    if x.find(".")!= -1 or x.find(",")!=-1:
        main()
    y = a[1]
    if y.find(".")!= -1 or y.find(",")!=-1:
        main()
    x, y = int(x), int(y)
    s = (x/y)*100
    return s
    #print('neispravan unos, ispravan unos je "X/Y", bey nula u imeniocu, probajte ponovo.')
def gauge(procenat):
 #   x , y = procenat
  #  x, y = int(x), int(y)
    b = procenat #((x/y)*100)
    if b <=1:
        print('E')
        return(f"E")
    elif b>=99:
        print('F')
        return(f"F")
    else:
        print(f'{(round(b))}%')
        return(f'{(round(b))}%')
if __name__=='__main__':
    main()