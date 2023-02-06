a = input('What is the Answer to the Great Question of Life, the Universe and Everything? ').lower().strip()
if a == '42':
    print("yes")
elif str(a) == 'forty two':
    print("yes")
elif str(a)=='forty-two':
    print("yes")
elif str(a)=='fortytwo':
    print("yes")
else:
    print("no")