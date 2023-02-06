meseci = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
dmeseci = {
    "January":'1',
    "February":'2',
    "March":'3',
    "April":'4',
    "May":'5',
    "June":'6',
    "July":'7',
    "August":'8',
    "September":'9',
    "October":'10',
    "November":'11',
    "December":'12'
}
while True:
    try:
        inicijal= input('Date: ')
        mesec , dan , godina=inicijal.split("/")
        if len (mesec) >2:
            continue
        if int(dan) >31:
            continue
        if int(mesec) >12:
            continue
        if dan in meseci:
            continue
        elif godina in meseci:
            continue
        elif len(dan)> 2 or len(godina)>4:
            continue
        break
    except:
        try:
            mesec , kan , godina=inicijal.split(" ")
            inzar = kan.rindex(",")
            dan = kan[0:inzar]
            if int(dan) >31:
                continue
            if dan in meseci:
                continue
            elif godina in meseci:
                continue
            elif len(dan)> 2 or len(godina)>4:
                continue
            break
        except:
            continue
if mesec in meseci:
    mesec = dmeseci[mesec]
if len(dan)<2:
    dan1 = dan.zfill(2)
else: dan1 = dan
if len(mesec)<2:
    mesec =mesec.zfill(2)
elif len(mesec)==2:
   mesec=mesec
else: mesec = dmeseci[mesec]
print(f'{godina}-{mesec}-{dan1}')