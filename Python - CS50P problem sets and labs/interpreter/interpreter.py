x ,y ,z = input('Expression: ').split()
x, z = int(x), int(z)
if y == '+':
    print(round(float(x+z),1))
elif y == "/":
    print(round(float(x/z),1))
elif y =="*":
    print(round(float(x*z),1))
elif y =="-":
    print(round(float(x-z),1))
