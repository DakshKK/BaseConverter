digit = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
sign = '-'

def converter(number, fromBase, toBase):
    if number[0] == sign:
        neg, number = True, number[1:]
    else:
        neg = False

    number = number.lstrip('0')
    res = []

    if number:
        for val in number:
            res.append(val)
            for i in range(-2, -(len(res) + 1), -1):
                q, r = divmod(digit.index(res[i]) * fromBase + digit.index(res[i + 1]), toBase)
                res[i], res[i + 1] = digit[q], digit[r]

            baseValue = digit.index(res[0])
            while baseValue >= toBase:
                q, r = divmod(baseValue, toBase)
                res[0] = digit[r]
                baseValue = q
                res.insert(0, digit[baseValue])
            del baseValue

        if neg:
            res.insert(0, sign)

        return ''.join(res).lstrip('0')
    else:
        return '0'

def transform(number, fromDigit, toDigit, fromSign, toSign):
    if number[0] == fromSign:
        neg, number = True, number[1:]
    else:
        neg = False

    number = [toDigit[fromDigit.index(n)] for n in number]

    if neg:
        number.insert(0, toSign)

    return ''.join(number)

def convert(number, fromBase, toBase, data):
    number = transform(number, data['fromDigit'], digit, data['fromSign'], sign)
    number = converter(number, fromBase, toBase)
    number = transform(number, digit, data['toDigit'], data['fromSign'], data['toSign'])

    return number
