digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
sign = '-'

def convert(number, fromBase, toBase):
    if not validate(number, fromBase):
        raise ValueError(f'\x1b[6H\x1b[1mInvalid digits found in given number for base {fromBase}.\x1b[22m')

    if number[0] == '-':
        neg = True
        number = number[1:]
    else:
        neg = False

    number = number.lstrip('0')

    res = []
    if number:
        for digit in number:
            res.append(digit)
            for pos in range(-2, -(len(res) + 1), -1):
                q, r = divmod(digits.index(res[pos]) * fromBase + digits.index(res[pos + 1]), toBase)
                res[pos], res[pos + 1] = digits[q], digits[r]

            baseValue = digits.index(res[0])
            while baseValue >= toBase:
                q, r = divmod(baseValue, toBase)
                res[0] = digits[r]
                baseValue = q
                res.insert(0, digits[baseValue])
            del baseValue

        if neg:
            res.insert(0, '-')

        return ''.join(res).lstrip('0')
    else:
        return '0'

def validate(number, fromBase):
    num = number
    if number[0] == '-':
        num = number[1:]

    return all(sub in digits[:fromBase] for sub in num)
