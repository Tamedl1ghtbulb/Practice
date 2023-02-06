def main():
    a = input('Greeting: ')

    print('$'+str(value(a)))
    exit()
def value(greeting):
    greeting = greeting.lower().strip().split(" ")
    b = greeting[0][0]
    if greeting[0].startswith('hello'):
        return 0
    elif b=='h'  and not greeting[0].startswith('hello'):
        return 20
    else:
        return 100

if __name__ == '__main__':
    main()