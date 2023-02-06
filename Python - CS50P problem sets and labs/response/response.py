import validator_collection as va

a = input('What\'s your email adress? ')
try:
    o = va.checkers.is_email(a)
    if o:
        print('Valid')
    else:
        print('Invalid')
except:
    print('Invalid')