def main():
    a= input()
    convert(a)

def convert(tekst):
    tekst=tekst.replace(":(","🙁")
    tekst = tekst.replace(":)","🙂")
    print(tekst)
main()