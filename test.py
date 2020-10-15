import converter

f = {
        'digit': 1234,
        'sign': '+'
        }
num = ['+24', 2, '+1']
assert(
        [converter.convert(n, f, {'sign': '/'}) for n in num]
        == ['/7', '1', '/0']
        ), 'Conversion was wrong'

converter.modifyFro(5)
converter.customTo(2468)
num = [24, 2, 10]
assert(
        [converter.convert(n) for n in num] == ['86', '6', '44']
        ), 'Conversion was wrong'

converter.modifyDef(5, 2)
num = [41, '024', 00]
assert(
        [converter.convert(n) for n in num] == ['10101', '1110', '0']
        ), 'Conversion was wrong'

converter.customDef('ABCD', '*', '-', 'DCBA', '+', '-')
num = ['DC', '*AD', '*DB', 'BAD']
assert(
        [converter.convert(n) for n in num] == ['AB', '+A', '+AC', 'CDA']
        ), 'Conversion was wrong'

converter.customFro('😁😃', sep = '➗')
converter.modifyTo(4)
num = ['-😁😃➗😁😃😃', '😁😃➗😃😁😃', '-😁😃😃😁']
assert(
        [converter.convert(n) for n in num] == ['-1.12', '1.22', '-12']
        ), 'Conversion was wrong'

converter.modifyFro(4)
t = {
        'digit': '😁😃',
        'sign': '-',
        'sep': '➗'
        }
num = [-1.3, -1.2, 2.13, .333]
assert(
        [converter.convert(n, to = t) for n in num]
         == ['-😃➗😃😃', '-😃➗😃', '😃😁➗😁😃😃😃', '😁➗😃😃😃😃😃😃']
        ), 'Conversion was wrong'
