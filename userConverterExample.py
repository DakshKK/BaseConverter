import sys
import time
from Converter import userConverter

print('\x1b[48;2;64;35;71m\x1b[38;2;255;255;255m\x1b[?1049h', end='')

digits = ''
toDigits = ''
sign = ''
toSign = ''

fromBase = int(input('Enter the base you are converting from, 0 for custom base: '))
if fromBase == 0:
    digits = input('Enter your custom digit space: ')
    sign = input('Enter the sign used for your digits space: ')
    fromBase = len(digits)
    if sign in digits or fromBase < 2:
        raise ValueError('Sign character found in digits')
        sys.exit('\x1b[?1049l\x1b[0m\n')

toBase = int(input('Enter the base you are converting to, 0 for custom base: '))
if toBase == 0:
    toDigits = input('Enter the digits of base to convert to, (0 if same): ')
    if toDigits == '0':
        toDigits = digits
        toSign = sign
    else:
        toSign = input('Enter the sign for your custom base: ')
    toBase = len(toDigits)
    if toSign in toDigits or toBase < 2:
        raise ValueError('Sign character found in digits')
        sys.exit('\x1b[?1049l\x1b[0m\n')

number = input('Enter the number you are converting in the correct base: ')

print(f'Converted num is: {userConverter.convert(number, fromBase, toBase, digits, toDigits, sign, toSign)}')

time.sleep(10)
print('\x1b[?1049l\x1b[0m')
