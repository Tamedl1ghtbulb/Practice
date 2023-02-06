import sys
from PIL import Image, ImageOps
from os.path import splitext
def main():
    try:
        if len(sys.argv)>3:
            sys.exit('Too many command-line arguemnts')
        elif len(sys.argv)<=1:
            sys.exit('Too few command-line arguments')
        elif str(sys.argv[1]).lower()[-4:] != '.jpg':
            sys.exit('Not a JPG file')
        elif str(sys.argv[2]).lower()[-4:] != '.jpg':
                    sys.exit('Not a JPG file')
        else:
            slika = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit('Slika ne postoji')

    majica = Image.open('shirt.png')
    velicina = majica.size
    l = ImageOps.fit(slika,velicina)
    l.paste(majica, majica)
    l.save(sys.argv[2])

if __name__ =='__main__':
    main()
