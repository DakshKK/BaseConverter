from . import converter

'''
    def userConvert(number, fromBase, toBase, digits):
        number = number.lstrip('0')
'''

def transform(number, fromDigit, toDigit, fromSign, toSign):
    if number[0] == fromSign:
        neg = True
        number = number[1:]
    else:
        neg = False

    number = [toDigit[fromDigit.index(n)] for n in number]

    if neg:
        number.insert(0, toSign)

    return ''.join(number)

def convert(number, fromBase, toBase, digits, toDigits, sign = '-', toSign = '-'):
    if validateDigits(digits) or validateDigits(toDigits):
        raise ValueError('Invalid digit space.')

    if digits.strip():
        number = transform(number, digits, converter.digits, sign, '-')

    number = converter.convert(number, fromBase, toBase)

    if toDigits.strip():
        if toDigits == '0':
            number = transform(number, converter.digits, digits, '-', sign)
        else:
            number = transform(number, converter.digits, toDigits, sign, toSign)

    return number

def validateDigits(digits):
    return (len(digits) != len(set(digits)))
