"""Converter program to convert between bases.

Given a number, it converts from a given fromBase/fromDigit, to a given toBase/toDigit.
Before conversion, first change your from and to base either using one of the methods
or passing a custom one to convert.
"""

sysDigit = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
sysSign = '-'

fro = {
        'digit': sysDigit,
        'sign': sysSign,
        'base': 36
        }

to = {
        'digit': sysDigit,
        'sign': sysSign,
        'base': 36
        }

def modifyFro(froBase):
    '''
    Input argument is the base length.
    For fro
      - Digit gets modified to sysDigit[:froBase]
      - Sign becomes default sign '-'
      - Base becomes input provided
    '''

    fro['digit'] = sysDigit[:froBase]
    fro['sign'] = sysSign
    fro['base'] = froBase

def modifyTo(toBase):
    '''
    Input argument is the base length.
    For to
      - Digit gets modified to sysDigit[:toBase]
      - Sign becomes default sign '-'
      - Base becomes input provided
    '''

    to['digit'] = sysDigit[:toBase]
    to['sign'] = sysSign
    to['base'] = toBase

def modifyDef(froBase, toBase):
    '''
    Input argument is the fro and to Base length.
    Calls both modifyFro and modifyTo
    '''

    modifyFro(froBase)
    modifyTo(toBase)

def customFro(digit = sysDigit, sign = sysSign):
    '''
    Input arguments are digit space, and sign
    For fro
      - Digit gets modified to digit, default is system digit
      - Sign becomes sign, default is '-'
      - Base becomes len of digit
    '''

    fro['digit'] = str(digit)
    fro['sign'] = str(sign)
    fro['base'] = len(fro['digit'])

def customTo(digit = sysDigit, sign = sysSign):
    '''
    Input arguments are digit space, and sign
    For to
      - Digit gets modified to digit, default is system digit
      - Sign becomes sign, default is '-'
      - Base becomes len of digit
    '''

    to['digit'] = str(digit)
    to['sign'] = str(sign)
    to['base'] = len(to['digit'])

def customDef(froDigit = sysDigit, froSign = sysSign, toDigit = sysDigit, toSign = sysSign):
    '''
    Input arguments are digit space, and sign for both fro and to
    Calls customFro, and customTo, with respective arguments
    '''

    customFro(froDigit, froSign)
    customTo(toDigit, toSign)

def converter(number, fBase, tBase):
    '''
    Implements the algorithm to convert between two bases.
    '''

    if number[0] == sysSign:
        neg, number = True, number[1:]
    else:
        neg = False

    number = number.lstrip('0')
    res = []

    if number:
        for val in number:
            res.append(val)
            for i in range(-2, -(len(res) + 1), -1):
                q, r = divmod(sysDigit.index(res[i]) * fBase + sysDigit.index(res[i + 1]), tBase)
                res[i], res[i + 1] = sysDigit[q], sysDigit[r]

            base = sysDigit.index(res[0])
            while base >= tBase:
                q, r = divmod(base, tBase)
                res[0], base = sysDigit[r], q
                res.insert(0, sysDigit[base])
            del base

        res = list(''.join(res).lstrip('0'))
        if neg:
            res.insert(0, sysSign)

        return ''.join(res)
    else:
        return '0'

def transform(number, fDigit, tDigit, fSign, tSign):
    '''
    Transforms from user defined base to system defined base.
    '''

    if number[0] == fSign:
        neg, number = True, number[1:]
    else:
        neg = False

    number = [tDigit[fDigit.index(n)] for n in number]

    if neg:
        number.insert(0, tSign)

    return ''.join(number)

def validate(fro, to):
    '''
    Validates the input by checking if sign is in digit space, or digit space is unique or not.
    '''

    if fro['sign'] in fro['digit'] or to['sign'] in to['digit']:
        print('Sign found in digit.')
        return False
    if len(fro['digit']) != len(set(fro['digit'])) or len(to['digit']) != len(set(to['digit'])):
        print('Digit space is not unique.')
        return False
    if not (1 < fro['base'] < 37) or not (1 < to['base'] < 37):
        print('Invalid base. Can not convert.')
        return False
    return True

def convert(number, f = fro, t = to):
    '''
    Validates user input, after which if valid, converts the number.
    '''

    if f != fro:
        customFro(**f)
        f = fro
    if t != to:
        customTo(**t)
        t = to

    if validate(f, t):
        number = str(number)
        number = transform(number, f['digit'], sysDigit, f['sign'], sysSign)
        number = converter(number, f['base'], t['base'])
        number = transform(number, sysDigit, t['digit'], sysSign, t['sign'])
        return number
