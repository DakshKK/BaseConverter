[![GitHub repo size](https://img.shields.io/github/repo-size/DakshKK/BaseConverter?style=flat-square)](#)
[![License](https://img.shields.io/github/license/DakshKK/BaseConverter?style=flat-square)](LICENSE)
[![Maintenance](https://img.shields.io/maintenance/yes/2020?style=flat-square)](#)

# BaseConverter

  BaseConverter is a calculator written to convert numbers betwewen arbitrary bases. It takes a direct approach of converting the number without first shifting to decimal base.

## WHAT IT IS
  Since Python's `int` function has the shortcoming of only converting to base `10`, this program was developed to let you convert to arbitrary bases, that `int` can convert from, i.e. `2` to `36`.

  This program also gives you the additional feature, to let you convert custom defined bases, to a system defined, or another custom defined one.

  Hence the conversion of `(102421)`<sub>`5`</sub> to base `32` is successful as shown in the provided screenshot.

  &emsp;&emsp; ![](output.png?raw=true)

  And also the conversion of `*BAD` with the from and to digit spaces, respecetively defined as
```python3
f = {
    'digit': 'ABCDE',
    'sign': '*'
    } # Base is derived as len(digit)
t = {
    'digit': 'CD',
    'sign': '+'
    } # Base is derived as len(digit)
```
  is successful. And it transforms to `+DDDCC`.


### TODO
  - [x] Implement a system to let user enter their own system of digit, and accordingly convert inspired by [python-baseconv](https://github.com/semente/python-baseconv 'Base Converter, which uses decimal algorithm for conversion between bases.')
  - [x] Include working examples in a separate file, which imports the package, and tests it
  - [x] Implement floating point conversion
  - [x] Let user specify precision of conversion wanted
  - [ ] Write a PyPI package for this repo, so users can utilise it more easily, by doing a `pip install`
  - [ ] Implement `n`'s and `(n-1)`'s complement method of calculation

#### INFO
  - User can now convert using their own digit space, of any base. (Base is defined as length of your digit space. Hence `'abcd1234'`, is Base `8`)
  - Base is case-sensitive, hence `A` and `a` are not same
  - **Repeated characters in base, or sign in digit-space, will lead to error, just as it should.**
  - Program will calculate the base on its own for your given custom base input. Hence you need only to enter any of the digit-space, sign, and/or separator
  - There is some loss in accuracy in conversion of floating points, as would be expected, hence the output if feeded back, may not give the exact input back

### FUNCTIONS AND MODULE VARIABLES
  - A few variables as defined in the module are:
    - `sys` - A dictionary containing the system defined values as follows:
      - `'digit'` - The system maximum base digit space **`'0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'`**
      - `'sign'` - The system negative symbol **`-`**
      - `'sep'` - The system defined separator **`.`**
      - `'prec'` - The default precision **`6`**
    - `f` - A dictionary containing the data for the from base
    - `t` - A dictionary containing the data for the to base
    - `f` and `t` have the same keyword values as `sys`, with the expection of `'prec'`, instead there is `'base'`, which is the length of `'digit'`

  <br />

  - To facilitate easy definition and modification of bases, a few functions have been provided:
    - `setPrec(pre = 6)` - Used to set the precision, resetting to `6` on no args
    - `modifyF(fBase = 36)` - With no arguments resets `f` to the system base `36`
    - `modifyT(tBase = 36)` - With no arguments resets `t` to the system base `36`
    - `modifyDef(fBase, tBase)` - calls both `modifyF` and `modifyT`
    - `customF(digit = sys['digit'], sign = sys['sign'], sep = sys['sep'])` - Sets the respective values in `f` with the data passed or with system defaults, in `sys`
    - `customT(digit = sys['digit'], sign = sys['sign'], sep = sys['sep'])` - Sets the respective values in `t` with the data passed or with system defaults, in `sys`
    - `customDef(fDigit = sys['digit'], fSign = sys['sign'], fSep = sys['sep'],
        tDigit = sys['digit'], tSign = sys['sign'], tSep = sys['sep'])` - Calls both `customF` and `customT` with the data passed
    - `converter(number, digit, sign)` - Uses the algorithm explained in [`explanation.md`](explanation.md 'Explanation written for how the algorithm operates and calculates') to convert the number in integer form
    - `fraction(number, digit, sign, pre)` - Uses the algorithm explained in [`explanation.md`](explanation.md 'Explanation written for how the algorithm operates and calculates') to convert the number in its fractional form
    - `transform(number)` - Transforms number from that defined in `f` to that in `t`
    - `validate()` - Validates if the digit space, and corresponding data is valid
    - `numberCheck(number)` - Validates if input number is valid in defined `f` digit space
    - `convert(number, fro = f, to = t, pre = 0)` - The function which makes all the magic happen normally speaking
      - `fro` is a **dictionary** used for **single conversion** custom Base
      - `to` is a **dictionary** used for **single conversion** custom Base
      - `pre` is an **int** to set precision for only **one conversion**

### NOTES
  - If when defining a custom Base, using `customF` or `customT`, instead of wanting to pass, individual arguments, you can pass a dictionary containing any of the following keywords, in the given manner **`customF(**<dict-name>)`**, or **`customT(**<dict-name>)`**:
    - `'digit'` - The digit space
    - `'sign'` - The sign to be used
    - `'sep'` - The separator to be used
  - If it is being done via `customDef`, then it is to be passed in the same manner as above, and the keywords to be present in the dictionary are:
    - `'fDigit'` - The digit space for `f`
    - `'fSign'` - The sign to be used for `f`
    - `'fSep'` - The separator to be used for `f`
    - `'tDigit'` - The digit space for `t`
    - `'tSign'` - The sign to be used for `t`
    - `'tSep'` - The separator to be used for `t`

### EXAMPLES
  To see a few working tests you can check the [`test.py`](test.py 'Tests for the program.') file.

### EXPLANATION
  To understand how the algorithm works, please check [`explanation.md`](explanation.md 'Explanation written for how the algorithm operates and calculates').

### Install and Usage
  The repo can be directly cloned, and you can import the module in current directory.

  Example usage:

```python3
>>> # To use user defined bases
>>> import converter
>>> fro = {
... 'digit': '24',
... 'sign': '*',
... }
>>> converter.convert('*244242', t = {'digit': 24681379}, f = fro)
'+86'
>>>
>>> # To use a system defined fro, and user defined to
>>> converter.modifyF(5) # Modifies your fro base to 5, and digit space to '01234'
>>> converter.customT(2468)
>>> converter.convert(21)
'68'
>>>
>>> # For user defined fro, and system to, just pass fro as f = <dict-name>
>>> # And first modify to using converter.modifyT(<base>)
>>> # For both system defined, we can call the modify functions seperately or
>>> # modifyDef(<froBase>, <toBase>) can be called
>>> converter.modifyDef(5, 32)
>>> converter.convert('00141')
'1E'
>>>
>>> converter.customF('😁😃', sep = '➗')
>>> converter.modifyT(4)
>>> converter.convert('-😁😃😃😁')
'-12'
>>> converter.convert('-😁😃➗😁😃😃')
'-1.12'
>>> converter.convert('😁😃➗😃😁😃')
'1.22'
>>>
>>> converter.modifyF(4)
>>> converter.customT('😁😃', sep = '➗')
>>> converter.convert(-1.3)
'-😃➗😃😃'
>>> converter.convert(-1.12)
'-😃➗😁😃😃'
>>> converter.setPrec(4)
>>> converter.convert(.123)
'-😁➗😁😃😃😁'
>>> converter.convert(.123, pre = 10)
'-😁➗😁😃😃😁😃😃'
```

  To get a list of functions in the module run `dir(converter)`, or `help(converter)`.

  To get help on respective functions run `help(converter.<function-name>)`.
