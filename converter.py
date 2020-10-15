"""Converter program to convert between bases.

Given a number, it converts from a given fromBase/fromDigit, to a given toBase/toDigit.
Before conversion, first change your from and to base either using one of the methods
or passing a custom one to convert.
"""

digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
negsym = '-'
sepr = '.'

f = {
        'digit': digits,
        'sign': negsym,
        'sep' : sepr,
        'base': 36
        }

t = {
        'digit': digits,
        'sign': negsym,
        'sep' : sepr,
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
    f['sep'] = sepr
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
    t['sep'] = sepr
    t['base'] = toBase

def modifyDef(froBase, toBase):
    '''
    Input argument is the fro and to Base length.
    Calls both modifyFro and modifyTo
    '''

    modifyFro(froBase)
    modifyTo(toBase)

def customFro(digit = digits, sign = negsym, sep = sepr):
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

def customTo(digit = digits, sign = negsym, sep = sepr):
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

def customDef(froDigit = digits, froSign = negsym, froSep = sepr,
        toDigit = digits, toSign = negsym, toSep = sepr):
    '''
    Input arguments are digit space, and sign for both fro and to
    Calls customFro, and customTo, with respective arguments
    '''

    customFro(froDigit, froSign, froSep)
    customTo(toDigit, toSign, toSep)

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

        res = ''.join(res).lstrip(digit[0])
    else:
        res = digit[0]

    if neg:
        res = sign + res
    return res

def fraction(number, digit, sign):
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

        return ''.join(res).rstrip(digit[0])
    else:
        return digit[0]

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
        if numberCheck(number):
            if f['base'] >= t['base']:
                pSep = number.find(f['sep'])
                if pSep == -1:
                    number = converter(number, f['digit'], f['sign'])
                else:
                    number = converter(number[:pSep], f['digit'], f['sign']) \
                            + f['sep'] + \
                            fraction(number[pSep + 1:], f['digit'], f['sign'])
            number = transform(number)
            if f['base'] < t['base']:
                pSep = number.find(t['sep'])
                if pSep == -1:
                    number = converter(number, t['digit'], t['sign'])
                else:
                    number = converter(number[:pSep], t['digit'], t['sign']) \
                            + t['sep'] + \
                            fraction(number[pSep + 1:], t['digit'], t['sign'])
            return number
