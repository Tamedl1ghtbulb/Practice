import sys
import tabulate
konacno = []
try:
    if len(sys.argv)>2:
        sys.exit('Too many command-line arguemnts')
    elif len(sys.argv)<=1:
        sys.exit('Too few command-line arguments')
    elif str(sys.argv[1]).lower()[-4:] != '.csv':
        sys.exit('Not a CSV file')
    else:
        with open(str(sys.argv[1])) as file:
            for line in file:
                linija = line.rstrip('\n').split(',')
                konacno.append(linija)
            print(tabulate.tabulate(konacno,tablefmt='grid',headers= 'firstrow'))
except FileNotFoundError:
    sys.exit('File not found')
