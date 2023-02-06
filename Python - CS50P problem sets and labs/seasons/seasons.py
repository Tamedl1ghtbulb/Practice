from datetime import date
from datetime import timedelta
import datetime
import re
import sys
import inflect
p = inflect.engine()
class Racun(object):
    def __init__(self):
        self.rodj = "1999-10-10"
        self.kraj = "1999-10-10"
    @property
    def rodj(self):
        return self._rodj

    @rodj.setter
    def rodj(self, rodj):
        if not re.match(r"^\d{4}\-(0?[1-9]|1[012])\-(0?[1-9]|[12][0-9]|3[01])$",str(rodj), re.IGNORECASE):
            sys.exit('Invalid date')
        self._rodj = rodj
    def __str__(self):
        return f'{p.number_to_words(self.razlika,andword="").capitalize()} minutes'
    def racunica(self):
        godina , mesec , dan = self.rodj.split('-')
        godina , mesec , dan = int(godina), int(mesec), int(dan)
        self.rodj = date(godina,mesec,dan)
        self.razlika = self.kraj - self.rodj
        self.razlika = self.razlika.days
        self.razlika = self.razlika * 24*60
        return self.razlika
def main():
    objekat =get_info()
   # print(objekat)

def get_info():
    racuni = Racun()
    racuni.rodj = input('Unesite datum kada ste rodjeni:')
    racuni.kraj = date.today()
    racuni.racunica()
    print(racuni)


if __name__ == "__main__":
    main()
