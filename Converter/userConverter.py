from . import converter

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

def convert(number, fromBase, toBase, data):
    number = transform(number, data['fromDigit'], converter.digits, data['fromSign'], converter.sign)
    number = converter.convert(number, fromBase, toBase)
    number = transform(number, converter.digits, data['toDigit'], data['fromSign'], data['toSign'])

    return number
