"""Converter program to convert between bases.

Given a number, it converts from a given fromBase/fromDigit, to a given toBase/toDigit.
Before conversion, first change your from and to base either using one of the methods
or passing a custom one to convert.
"""

digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
negsym = '-'

f = {
        'digit': digits,
        'sign': negsym,
        'base': 36
        }

t = {
        'digit': digits,
        'sign': negsym,
        'base': 36
        }

def modifyFro(froBase):
    '''
    Input argument is the base length.
    For fro
      - Digit gets modified to digits[:froBase]
      - Sign becomes default sign '-'
      - Base becomes input provided
    '''

    f['digit'] = digits[:froBase]
    f['sign'] = negsym
    f['base'] = froBase

def modifyTo(toBase):
    '''
    Input argument is the base length.
    For to
      - Digit gets modified to digits[:toBase]
      - Sign becomes default sign '-'
      - Base becomes input provided
    '''

    t['digit'] = digits[:toBase]
    t['sign'] = negsym
    t['base'] = toBase

def modifyDef(froBase, toBase):
    '''
    Input argument is the fro and to Base length.
    Calls both modifyFro and modifyTo
    '''

    modifyFro(froBase)
    modifyTo(toBase)

def customFro(digit = digits, sign = negsym):
    '''
    Input arguments are digit space, and sign
    For fro
      - Digit gets modified to digit, default is system digit
      - Sign becomes sign, default is '-'
      - Base becomes len of digit
    '''

    f['digit'] = str(digit)
    f['sign'] = str(sign)
    f['base'] = len(f['digit'])

def customTo(digit = digits, sign = negsym):
    '''
    Input arguments are digit space, and sign
    For to
      - Digit gets modified to digit, default is system digit
      - Sign becomes sign, default is '-'
      - Base becomes len of digit
    '''

    t['digit'] = str(digit)
    t['sign'] = str(sign)
    t['base'] = len(t['digit'])

def customDef(froDigit = digits, froSign = negsym, toDigit = digits, toSign = negsym):
    '''
    Input arguments are digit space, and sign for both fro and to
    Calls customFro, and customTo, with respective arguments
    '''

    customFro(froDigit, froSign)
    customTo(toDigit, toSign)

def converter(number, digit, sign):
    '''
    Implements the algorithm to convert between two bases.
    '''

    if number[0] == sign:
        neg, number = True, number[1:]
    else:
        neg = False

    number = number.lstrip(digit[0])
    res = []

    if number:
        for val in number:
            res.append(val)
            for i in range(-2, -(len(res) + 1), -1):
                q, r = divmod(digit.index(res[i]) * f['base']
                        + digit.index(res[i + 1]), t['base'])
                res[i], res[i + 1] = digit[q], digit[r]

            base = digit.index(res[0])
            while base >= t['base']:
                q, r = divmod(base, t['base'])
                res[0], base = digit[r], q
                res.insert(0, digit[base])

        res = ''.join(res).lstrip(digit[0])
        if neg:
            res = sign + res
    else:
        res = digit[0]
    return res

def transform(number):
    '''
    Transforms from user defined base to system defined base.
    '''

    if number[0] == f['sign']:
        neg, number = True, number[1:]
    else:
        neg = False

    number = ''.join(
            [t['digit'][f['digit'].index(n)] for n in number]
            )

    if neg:
        number = t['sign'] + number
    return number

def validate():
    '''
    Validates the input by checking if sign is in digit space, or digit space is unique or not.
    '''

    if f['sign'] in f['digit'] or t['sign'] in t['digit']:
        print('Sign found in digit.')
        return False
    if len(f['digit']) != len(set(f['digit'])) or len(t['digit']) != len(set(t['digit'])):
        print('Digit space is not unique.')
        return False
    return True

def convert(number, fro = f, to = t):
    '''
    Validates user input, after which if valid, converts the number.
    '''

    if fro != f:
        customFro(**fro)
        fro = f
    if to != t:
        customTo(**to)
        to = t

    if validate():
        number = str(number)
        if f['base'] >= t['base']:
            number = converter(number, f['digit'], f['sign'])
        number = transform(number)
        if f['base'] < t['base']:
            number = converter(number, t['digit'], t['sign'])
        return number
