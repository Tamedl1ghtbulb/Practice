import sys
count = 0
try:
    if len(sys.argv)>2:
        sys.exit('Too many command-line arguemnts')
    elif len(sys.argv)<=1:
        sys.exit('Too few command-line arguments')
    elif str(sys.argv[1])[-3:] != '.py':
        sys.exit('Not a Python file')
    else:
        with open(str(sys.argv[1])) as file:
            for row in file:
                if row.isspace():
                    count = count
                elif row.lstrip().startswith('#'):
                    count = count
                else:
                    count = count +1
except FileNotFoundError:
    sys.exit('File not found')
print(count)