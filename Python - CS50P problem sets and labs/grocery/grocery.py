d = []
while True:
    try:
        invoce = input().upper()
        d.append(invoce)
    except EOFError:
        break
d.sort()
l = {}
for i in d:
    if i in l:
        l[i] = l[i]+1
    else:
        l[i] = 1
for k , v in l.items():
    print(str(v)+" "+k)

