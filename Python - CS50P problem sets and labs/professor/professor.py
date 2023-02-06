#input nivoi 1,2 ili 3

#matematickig problema samo sa adicijom sa random x + y sa tim da broj cifara u x i y korespondira nivou

#prezentuj 10 mat problema ali ukoliko za pojedinacan problem bude 3 netacna odgovora izbaci odgovor i promtuj sledeci problem

#prikazi tacan rezultat (broj tacnih odgovora)
import random


def main():
    global rezultat
    global greska
    rezultat = 0
    greska = 0
    x= 0
    y = 0
    nivo = get_level()
    for i in range(10):
        x , y = generate_integer(nivo)
        testiranje(x,y)
    print('Score: '+ str(rezultat))


def get_level():
    while True:
        try:
            a = int(input('Level: '))
            if a >3 or a<1:
                continue
            else:
                return a
        except:
            continue

def generate_integer(level):
    if level == 1:
        x= random.randint(0,9)
        y= random.randint(0,9)
        return (x , y)
    if level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
        return (x , y)
    if level == 3:
        x = random.randint(100,999)
        y = random.randint(100,999)
        return (x , y)
def testiranje(x,y):
    while True:
        global rezultat
        global greska
        x = int(x)
        y = int(y)
        try:
            c = int(input((f'{str(x)} + {str(y)} =')))
        except:
            continue
        if c == x+y:
            rezultat = rezultat + 1
            greska = 0
            return
        else:
            print('EEE')
            greska = greska + 1
            if greska == 3:
                d = x +y
                print(d)
                greska = 0
                return
            else:
                continue
if __name__ == "__main__":
    main()
