import sys
import time

class Converter:
    def __init__(self, fromBase, toBase, digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        self.fromBase = fromBase
        self.toBase = toBase
        self.digits = digits

    def convert(self, number):
        number = number.lstrip('0')
        res = []
        if number:
            for digit in number:
                res.append(digit)
                for pos in range(-2, -(len(res) + 1), -1):
                    q, r = divmod(self.digits.index(res[pos]) * self.fromBase + self.digits.index(res[pos + 1]), self.toBase)
                    res[pos], res[pos + 1] = self.digits[q], self.digits[r]

                baseValue = self.digits.index(res[0])
                while baseValue >= self.toBase:
                    q, r = divmod(baseValue, self.toBase)
                    res[0] = self.digits[r]
                    baseValue = q
                    res.insert(0, self.digits[baseValue])
                del baseValue
            return ''.join(res).lstrip('0')
        else:
            return '0'

    def validate(self, number):
        return all(sub in self.digits[:self.fromBase] for sub in number)

if __name__ == '__main__':
    print('\x1b[48;2;64;35;71m\x1b[38;2;255;255;255m\x1b[?1049h', end='')

    try:
        fromBase = int(input('\x1b[HEnter the base you are converting from:\x1b[;42H'))
        if fromBase > 36 or fromBase < 2:
            raise ValueError
    except:
        print('\x1b[3H\x1b[1mInvalid Value for Base Entered.\x1b[22m')
        time.sleep(2)
        sys.exit('\x1b[?1049l\x1b[0m\n')
    else:
        try:
            toBase = int(input('\x1b[2HEnter the base you are converting to:\x1b[2;42H'))
            if fromBase == toBase or toBase > 36 or toBase < 2:
                raise ValueError
        except:
            print('\x1b[4H\x1b[1mInvalid Value for Base Entered.\x1b[22m')
            time.sleep(2)
            sys.exit('\x1b[?1049l\x1b[0m\n')

    conv = Converter(fromBase, toBase)

    try:
        number = input('\x1b[4HEnter the number to convert:\x1b[4;42H')
        number = number.upper()
        if conv.validate(number):
            pass
        else:
            raise ValueError
    except ValueError:
        print(f'\x1b[6H\x1b[1mInvalid literal {number} entered for base {fromBase}\x1b[22m')
    except:   
        print(f'\x1b[6H\x1b[1mInvalid number entered for base {fromBase}\x1b[22m')
    else:
        print(f'Converted number is:\x1b[5;42H{conv.convert(number)}')

    try:
        time.sleep(10)
    except:
        pass
    finally:
        print('\x1b[?1049l\x1b[0m\n', end='')
