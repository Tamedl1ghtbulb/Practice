import csv

import sys
konacno = []
try:
    if len(sys.argv)>3:
        sys.exit('Too many command-line arguemnts')
    elif len(sys.argv)<=1:
        sys.exit('Too few command-line arguments')
    elif str(sys.argv[1]).lower()[-4:] != '.csv':
        sys.exit('Not a CSV file')
    else:
        with open(sys.argv[1],'r')as file:
            reader= csv.DictReader(file)
            for line in reader:
                a= line['name'].split(',')
                b = {'first': a[1].lstrip(), 'last': a[0], 'house':line['house']}
                konacno.append(b)
    with open('after.csv','w',newline='') as file:
        s = ['first','last','house']
        writer = csv.writer(file)
        writer.writerow(['first','last','house'])
        for i in konacno:
            writer.writerow(i)
except FileNotFoundError:
    sys.exit('File not found')
with open(sys.argv[2],'w') as fajl:
    writer = csv.DictWriter(fajl, fieldnames = ['first','last','house'])
    writer.writerow({'first':'first','last':'last','house':'house'})
    for red in konacno:
        writer.writerow({'first':red['first'], 'last':red['last'],'house':red['house']})