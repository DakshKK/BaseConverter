import time, sys
from Converter import userConverter

print('\x1b[48;2;64;35;71m\x1b[38;2;255;255;255m\x1b[?1049h', end='')

data = {
        'fromDigit': '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        'fromSign': '-',
        'toDigit': '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        'toSign': '-',
        }
quit = False

choice = int(input('''
 ____                  ____                          _            
| __ )  __ _ ___  ___ / ___|___  _ ____   _____ _ __| |_ ___ _ __ 
|  _ \ / _` / __|/ _ \ |   / _ \| '_ \ \ / / _ \ '__| __/ _ \ '__|
| |_) | (_| \__ \  __/ |__| (_) | | | \ V /  __/ |  | ||  __/ |   
|____/ \__,_|___/\___|\____\___/|_| |_|\_/ \___|_|   \__\___|_|   


    1. System to System
    2. System to User Defined
    3. User Defined to System
    4. User defined to User defined
        1. From- and To- base are same
        2. From- and To- base are different
    5. Exit

    Enter your Choice: '''))
print()
if choice == 1:
    fromBase = int(input('    Enter the Base you want to convert from: '))
    toBase = int(input('    Enter the Base you want to convert to: '))
elif choice == 2:
    fromBase = int(input('    Enter the Base you want to convert from: '))
    data['toDigit'] = input('    Enter the digit space you want to convert to: ')
    data['toSign'] = input('    Enter the sign used in your base: ')
    toBase = len(data['toDigit'])
elif choice == 3:
    data['fromDigit'] = input('    Enter the digit space you want to convert from: ')
    data['fromSign'] = input('    Enter the sign used in your base: ')
    fromBase = len(data['fromDigit'])
    toBase = int(input('    Enter the Base you want to convert to: '))
elif choice == 4:
    ch = int(input('\n    Please enter the conversion you want: '))
    data['fromDigit'] = input('    Enter the digit space you want to convert from: ')
    data['fromSign'] = input('    Enter the sign used in your base: ')
    fromBase = len(data['fromDigit'])
    if ch == 1:
        data['toDigit'] = data['fromDigit']
        data['toSign'] = data['fromSign']
        toBase = fromBase
    elif ch == 2:
        data['toDigit'] = input('    Enter the digit space you want to convert to: ')
        data['toSign'] = input('    Enter the sign used in your base: ')
        toBase = len(data['toDigit'])
elif choice == 5:
    time.sleep(2)
    sys.exit('\x1b[?1049l\x1b[0m')

if data['fromSign'] in data['fromDigit'] or data['toSign'] in data['toDigit']:
    print('\nSign found within digit space')
    quit = True
elif fromBase < 2 or toBase < 2:
    print('\nInvalid Base Entered')
    quit = True
elif len(data['fromDigit']) != len(set(data['fromDigit'])) or len(data['toDigit']) != len(set(data['toDigit'])):
    print('\nDigit space has repeated characters')
    quit = True

if quit:
    time.sleep(5)
    sys.exit('\x1b[?1049l\x1b[0m')

number = input('    Enter the number in your base to convert: ')

print(f"\n    Converted number is: {userConverter.convert(number, fromBase, toBase, data)}")

time.sleep(5)
print('\x1b[?1049l\x1b[0m')
