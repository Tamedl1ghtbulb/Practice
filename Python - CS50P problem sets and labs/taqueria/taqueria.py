d = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
ukupno = 0
while True:
    try:
        a = input('Item: ').title()
    except EOFError:
        print()
        break
    if a not in d:
        continue
    ukupno = ukupno + round(float(d[a]),2)
    print("${:.2f}".format(ukupno))