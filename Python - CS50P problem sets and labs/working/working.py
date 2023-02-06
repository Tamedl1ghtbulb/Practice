import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    tacnoprovera = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$",s)
    if tacnoprovera:
        delovi = tacnoprovera.groups()
        if int(delovi[1]) > 12 or int(delovi[5]) > 12:
            raise ValueError
        sat = delovi[1]
        minut = delovi[2]
        formati = delovi[3]
        sat1 = delovi[5]
        minut1 = delovi[6]
        formati1 = delovi[7]
        noviminut = minut
        noviminut1 = minut1
        if formati =='PM':
            if int(sat) ==12:
                novisat = 12
            else:
                novisat = int(sat)+12
        else:
            if int(sat) ==12:
                novisat = 0
            else:
                novisat = int(sat)
        if minut == None:
            noviminut = ':00'
            novovreme = f"{novisat:02}"+noviminut
        else:
            novovreme = f"{novisat:02}"+':'+noviminut
        if formati1 =='PM':
            if int(sat1) ==12:
                novisat1 = 12
            else:
                novisat1 = int(sat1)+12
        else:
            if int(sat1) ==12:
                novisat1 = 0
            else:
                novisat1 = int(sat1)
        if minut1 == None:
            noviminut1 = ':00'
            novovreme1 = f"{novisat1:02}"+noviminut1
        else:
            novovreme1 = f"{novisat1:02}"+':'+noviminut1
        return novovreme+' to '+novovreme1
    else:
        raise ValueError

...


if __name__ == "__main__":
    main()
