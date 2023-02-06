import pyfiglet
import sys
sve = pyfiglet.FigletFont.getFonts()
if len(sys.argv) ==1:
    a= input()
    b = pyfiglet.Figlet()
    print(b.renderText(a))
elif len(sys.argv) ==3:
    if sys.argv[1] == "-f":
        if sys.argv[2] not in sve:
            sys.exit('Invalid Font.')
        a= input()
        b= pyfiglet.Figlet(font=str(sys.argv[2]))
        print(b.renderText(a))
    elif sys.argv[1] == "--font":
        if sys.argv[2] not in sve:
            sys.exit('Invalid Font.')
        a= input()
        b= pyfiglet.Figlet(font=str(sys.argv[2]))
        print(b.renderText(a))
    else:
        sys.exit('ispravan parametar je -f ili --font')
else:
    sys.exit('Netacan unos parametara')


