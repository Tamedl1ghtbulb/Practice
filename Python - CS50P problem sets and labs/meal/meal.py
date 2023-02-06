def main():
    a = input('What time is it? ')
    convert(a)

def convert(time):
    sat , minut = time.split(':')
    deosata= float(minut)/60
    ukflo = float(sat) + deosata
    if ukflo >= 7 and ukflo<=8:
        print('breakfast time' )
    elif ukflo >=12 and ukflo<=13:
        print('lunch time')
    elif ukflo >=18 and ukflo<=19:
        print('dinner time',)
#    else:

if __name__ == "__main__":
    main()
