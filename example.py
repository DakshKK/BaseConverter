import time, sys
import converter

def menu() -> int:
    return int(input(
    '''
\x1b[1H  ____                  ____                          _            
\x1b[2H | __ )  __ _ ___  ___ / ___|___  _ ____   _____ _ __| |_ ___ _ __ 
\x1b[3H |  _ \ / _` / __|/ _ \ |   / _ \| '_ \ \ / / _ \ '__| __/ _ \ '__|
\x1b[4H | |_) | (_| \__ \  __/ |__| (_) | | | \ V /  __/ |  | ||  __/ |   
\x1b[5H |____/ \__,_|___/\___|\____\___/|_| |_|\_/ \___|_|   \__\___|_|   


    1. System to System
    2. System to User Defined
    3. User Defined to System
    4. User defined to User defined
    5. Exit

    Enter your Choice: '''))

def setup(choice: int):
    global fro, to
    if choice == 1:
        fro['base'] = int(input('    Enter the Base you want to convert from: '))
        to['base'] = int(input('    Enter the Base you want to convert to: '))
        fro['digit'] = fro['digit'][:fro['base']]
        to['digit'] = to['digit'][:to['base']]
    elif choice == 2:
        fro['base'] = int(input('    Enter the Base you want to convert from: '))
        fro['digit'] = fro['digit'][:fro['base']]
        to['digit'] = input('    Enter the digit space you want to convert to: ')
        to['sign'] = input('    Enter the sign used in your base: ')
        to['base'] = len(to['digit'])
    elif choice == 3:
        fro['digit'] = input('    Enter the digit space you want to convert from: ')
        fro['sign'] = input('    Enter the sign used in your base: ')
        fro['base'] = len(fro['digit'])
        to['base'] = int(input('    Enter the Base you want to convert to: '))
        to['digit'] = to['digit'][:to['base']]
    elif choice == 4:
        fro['digit'] = input('    Enter the digit space you want to convert from: ')
        fro['sign'] = input('    Enter the sign used in your base: ')
        fro['base'] = len(fro['digit'])
        to['digit'] = input('    Enter the digit space you want to convert to: ')
        to['sign'] = input('    Enter the sign used in your base: ')
        to['base'] = len(to['digit'])
    elif choice == 5:
        time.sleep(2)
        sys.exit('\x1b[?1049l\x1b[0m')

if __name__ == '__main__':
    print('\x1b[48;2;64;35;71m\x1b[38;2;255;255;255m\x1b[?1049h', end='')
    
    fro = {
            'digit': '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ',
            'sign': '-',
            }
    to = {
            'digit': '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ',
            'sign': '-',
            }
    quit = False
    
    choice = menu()
    print()
    setup(choice)

    if fro['sign'] in fro['digit'] or to['sign'] in to['digit']:
        print('\nSign found within digit space')
        quit = True
    elif fro['base'] < 2 or to['base'] < 2:
        print('\nInvalid Base Entered')
        quit = True
    elif len(fro['digit']) != len(set(fro['digit'])) or len(to['digit']) != len(set(to['digit'])):
        print('\nDigit space has repeated characters')
        quit = True
    
    if quit:
        pass
    else:
        number = input('    Enter the number in your base to convert: ')
        print(f"\n    Converted number is: {converter.convert(number, fro, to)}")
        
    time.sleep(5)
    print('\x1b[?1049l\x1b[0m')
