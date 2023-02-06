import sys
def main():
    a = input('Unesi nesto: ')
    print(shorten(a))
    exit()
def shorten(word):
    a = list(word)
    samoglasnici = ['a','e','i','o','u','A','E','I','O','U']
    b=[]
    for i in a:
        if i in samoglasnici:
            continue
        else:
            b.append(i)
    b = "".join(b)
    return b

if __name__ == "__main__":
    main()
