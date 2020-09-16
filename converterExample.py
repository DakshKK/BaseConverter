import sys
import time
from Converter import converter

print('\x1b[48;2;64;35;71m\x1b[38;2;255;255;255m\x1b[?1049h', end='')

try:
    fromBase = int(input('\x1b[HEnter the base you are converting from:\x1b[;42H'))
    if fromBase > 36 or fromBase < 2:
        raise ValueError
except:
    print('\x1b[3H\x1b[1mInvalid Value for Base Entered.\x1b[22m')
    time.sleep(2)
    sys.exit('\x1b[?1049l\x1b[0m\n')
else:
    try:
        toBase = int(input('\x1b[2HEnter the base you are converting to:\x1b[2;42H'))
        if fromBase == toBase or toBase > 36 or toBase < 2:
            raise ValueError
    except:
        print('\x1b[4H\x1b[1mInvalid Value for Base Entered.\x1b[22m')
        time.sleep(2)
        sys.exit('\x1b[?1049l\x1b[0m\n')

number = input('\x1b[4HEnter the number to convert:\x1b[4;42H')
number = number.upper()
print(f'Converted number is:\x1b[5;42H{converter.convert(number, fromBase, toBase)}')

try:
    time.sleep(10)
except:
    pass
finally:
    print('\x1b[?1049l\x1b[0m\n', end='')
