import requests
import sys
if len(sys.argv)==1:
    sys.exit('Missing command-line argument')
if len(sys.argv)>2:
    sys.exit('Too many command-line arguments')
try:
    a = float(sys.argv[1])
except:
    print('Command-line argument is not a number')
try:
    p = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    p = p.json()
except requests.RequestException:
    sys.exit()
cena = p['bpi']['USD']['rate']
cena = cena.replace(',',"")
rezultat = float(cena)*a
rezultat ='{:,.4f}'.format(rezultat)
print(f'${str(rezultat)}')