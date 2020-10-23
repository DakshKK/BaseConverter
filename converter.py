"""Converter program to convert between bases.

Given a number, it converts from a given fBase/fDigit, to a given tBase/tDigit.
Before conversion, first change your from and to base either using one of the methods
or passing a custom one to convert.
"""

sys = {
        'digit': '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ',
        'sign': '-',
        'sep': '.',
        'prec': 6
        }

f = {
        'digit': sys['digit'],
        'sign': sys['sign'],
        'sep' : sys['sep'],
        'base': 36
        }

t = {
        'digit': sys['digit'],
        'sign': sys['sign'],
        'sep' : sys['sep'],
        'base': 36
        }

def setPrec(pre = 6):
    '''
    A function to set the precision of floating point conversion
    '''

    sys['prec'] = pre

def modifyF(fBase = 36):
    '''
    Input argument is the base length.
    For fro
      - Digit gets modified to sys['digit'][:fBase]
      - Sign becomes default sign '-'
      - Base becomes input provided
    '''

    f['digit'] = sys['digit'][:fBase]
    f['sign'] = sys['sign']
    f['sep'] = sys['sep']
    f['base'] = fBase

def modifyT(tBase = 36):
    '''
    Input argument is the base length.
    For to
      - Digit gets modified to sys['digit'][:tBase]
      - Sign becomes default sign '-'
      - Base becomes input provided
    '''

    t['digit'] = sys['digit'][:tBase]
    t['sign'] = sys['sign']
    t['sep'] = sys['sep']
    t['base'] = tBase

def modifyDef(fBase = 36, tBase = 36):
    '''
    Input argument is the fro and to Base length.
    Calls both modifyF and modifyT
    '''

    modifyF(fBase)
    modifyT(tBase)

def customF(digit = sys['digit'], sign = sys['sign'], sep = sys['sep']):
    '''
    Input arguments are digit space, and sign
    For fro
      - Digit gets modified to digit, default is system digit
      - Sign becomes sign, default is '-'
      - Base becomes len of digit
    '''

    f['digit'] = str(digit)
    f['sign'] = str(sign)
    f['sep'] = str(sep)
    f['base'] = len(f['digit'])

def customT(digit = sys['digit'], sign = sys['sign'], sep = sys['sep']):
    '''
    Input arguments are digit space, and sign
    For to
      - Digit gets modified to digit, default is system digit
      - Sign becomes sign, default is '-'
      - Base becomes len of digit
    '''

    t['digit'] = str(digit)
    t['sign'] = str(sign)
    t['sep'] = str(sep)
    t['base'] = len(t['digit'])

def customDef(fDigit = sys['digit'], fSign = sys['sign'], fSep = sys['sep'],
        tDigit = sys['digit'], tSign = sys['sign'], tSep = sys['sep']):
    '''
    Input arguments are digit space, and sign for both fro and to
    Calls customF, and customT, with respective arguments
    '''

    customF(fDigit, fSign, fSep)
    customT(tDigit, tSign, tSep)

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
                base, r = divmod(base, t['base'])
                res[0] = digit[r]
                res.insert(0, digit[base])

    res = sign + (''.join(res).lstrip(digit[0]) or digit[0])

    if neg:
        return res
    else:
        return res[1:]

def fraction(number, digit, sign, pre):
    '''
    Implements the algorithm to convert between fractional part of two bases.
    '''

    number = number.rstrip(digit[0])
    res = []

    if number:
        for val in number[::-1]:
            res.insert(0, val)
            for i in range(len(res)):
                q, r = divmod(digit.index(res[i]) * t['base'], f['base'])
                res[i] = digit[q]
                if i != (len(res) - 1):
                    r += digit.index(res[i + 1])
                if r >= f['base']:
                    res[i] = digit[digit.index(res[i]) + (r // f['base'])]
                    r %= f['base']
                if i == (len(res) - 1):
                    res.append(digit[r])
                else:
                    res[i + 1] = digit[r]

            while digit.index(res[-1]) >= t['base']:
                q, r = divmod(digit.index(res[-1]) * t['base'], f['base'])
                res[-1] = digit[q]
                if r >= f['base']:
                    res[-1] = digit[digit.index(res[-1]) + (r // f['base'])]
                    r %= f['base']
                res.append(digit[r])

        while len(res) < 6:
            q, r = divmod(digit.index(res[-1]) * t['base'], f['base'])
            res[-1] = digit[q]
            if r >= f['base']:
                res[-1] = digit[digit.index(res[-1]) + (r // f['base'])]
                r %= f['base']
            res.append(digit[r])
    return ''.join(res).rstrip(digit[0])[:pre] or digit[0]

def transform(number):
    '''
    Transforms from f base to t base.
    '''

    if number[0] == f['sign']:
        neg, number = True, number[1:]
    else:
        neg = False

    pSep = number.find(f['sep'])
    if pSep == -1:
        number = ''.join(
                [t['digit'][f['digit'].index(n)] for n in number]
                )
    else:
        number = ''.join(
                [t['digit'][f['digit'].index(n)] for n in number[:pSep]]
                ) + t['sep'] + ''.join(
                [t['digit'][f['digit'].index(n)] for n in number[pSep + 1:]]
                )

    if neg:
        number = t['sign'] + number
    return number

def validate():
    '''
    Validates the input by checking if sign is in digit space, or digit space is unique or not.
    '''

    if f['sep'] == f['sign'] or t['sep'] == t['sign']:
        print('Separtor and sign symbols are the same.')
        return False
    if f['sign'] in f['digit'] or t['sign'] in t['digit']:
        print('Sign found in digit.')
        return False
    if f['sep'] in f['digit'] or t['sep'] in t['digit']:
        print('Separator found in digit.')
        return False
    if len(f['digit']) != len(set(f['digit'])) or len(t['digit']) != len(set(t['digit'])):
        print('Digit space is not unique.')
        return False
    return True

def numberCheck(number):
    '''
    Validates if the user has entered a valid number in the defined digit space
    '''
    if not all([n in f['digit'] for n in number if n not in f['sep'] + f['sign']]):
        print('Invalid number entered.')
        return False
    if number.count(f['sep']) > 1:
        print('Invalid number entered.')
        return False
    if number.count(f['sign']) > 1 or (number.count(f['sign']) == 1
            and number[0] != f['sign']):
        print('Invalid number entered.')
        return False
    return True

def convert(number, fro = f, to = t, pre = 0):
    '''
    Validates user input, after which if valid, converts the number.
    '''

    if fro != f:
        customF(**fro)
    if to != t:
        customT(**to)

    if validate():
        number = str(number)
        if numberCheck(number):
            if f['base'] >= t['base']:
                pSep = number.find(f['sep'])
                if pSep == -1:
                    number = converter(number, f['digit'], f['sign'])
                else:
                    number = converter(number[:pSep], f['digit'], f['sign']) \
                            + f['sep'] + \
                            fraction(number[pSep + 1:], f['digit'], f['sign'], pre or sys['prec'])
            number = transform(number)
            if f['base'] < t['base']:
                pSep = number.find(t['sep'])
                if pSep == -1:
                    number = converter(number, t['digit'], t['sign'])
                else:
                    number = converter(number[:pSep], t['digit'], t['sign']) \
                            + t['sep'] + \
                            fraction(number[pSep + 1:], t['digit'], t['sign'], pre or sys['prec'])
            return number
