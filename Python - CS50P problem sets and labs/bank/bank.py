a = input('Greeting: ').lower().strip().split(" ")
b = a[0][0]
if a[0].startswith('hello'):
    print('$0',end="")
elif b=='h'  and not a[0].startswith('hello'):
    print('$20',end="")

else:
    print('$100',end="")