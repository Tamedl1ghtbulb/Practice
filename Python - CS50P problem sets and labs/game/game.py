from random import randint
def inpval(p):
    while True:
        try:
            i =int(input(p))
            if i<1:
                continue
            else:
                return i
        except:
            continue
k = 'Level: '
l = 'Guess: '
a =inpval(k)
b =inpval(l)
c = randint(1,a)
print(c)
while True:
    if b == c:
        print('Just right!')
        break
    elif b > c:
        print('Too large!')
    else:
        print('Too small!')
    b=inpval(l)