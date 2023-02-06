import inflect
p = inflect.engine()
lista = []
while True:
    try:
        ime =input('Unesite ime: ')
        lista.append(ime)
    except EOFError:
        break
if len(lista)>2:
    a = p.join(lista,)
else:
    a = p.join(lista, final_sep="")
print(f'Adieu, adieu, to {a}')