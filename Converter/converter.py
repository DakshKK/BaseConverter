digits='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def convert(number, fromBase, toBase):
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
        return ''.join(res).lstrip('0')
    else:
        return '0'

def validate(number, fromBase):
    return all(sub in digits[:fromBase] for sub in number)
