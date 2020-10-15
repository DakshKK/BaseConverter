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
  - [x] Implement a system to let user enter their own system of digits, and accordingly convert inspired by [python-baseconv](https://github.com/semente/python-baseconv 'Base Converter, which uses decimal algorithm for conversion between bases.')
  - [ ] Write a PyPI package for this repo, so users can utilise it more easily, by doing a `pip install`
  - [x] Include working examples in a separate file, which imports the package, and tests it
  - [x] Implement floating point conversion
  - [ ] Let user specify precision of conversion wanted
  - [ ] Implement `n`'s and `(n-1)`'s complement method of calculation

#### INFO
  - User can now convert using their own digit space, of any base. (Base is defined as length of your digit space. Hence `'abcd1234'`, is Base `8`.).
  - Base is case-sensitive, hence `A` and `a` are not same
  - **Repeated characters in base, or sign in digit-space, will lead to error, just as it should.**
  - Program will calculate the base on its own for your given custom base input. Hence you need only to enter, the digit-space, and/or the sign.
  - There is some loss in accuracy in conversion of floating points, as would be expected, hence the output if feeded back, may not give the exact input back.

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
>>> converter.modifyFro(5) # Modifies your fro base to 5, and digit space to '01234'
>>> converter.customTo(2468)
>>> converter.convert(21)
'68'
>>>
>>> # For user defined fro, and system to, just pass fro as f = <dict-name>
>>> # And first modify to using converter.modifyTo(<base>)
>>> # For both system defined, we can call the modify functions seperately or
>>> # modifyDef(<froBase>, <toBase>) can be called
>>> converter.modifyDef(5, 32)
>>> converter.convert('00141')
'1E'
>>>
>>> converter.customFro('😁😃', sep = '➗')
>>> converter.modifyTo(4)
>>> converter.convert('-😁😃😃😁')
'-12'
>>> converter.convert('-😁😃➗😁😃😃')
'-1.12'
>>> converter.convert('😁😃➗😃😁😃')
'1.22'
>>>
>>> converter.modifyFro(4)
>>> converter.customTo('😁😃', sep = '➗')
>>> converter.convert(-1.3)
'-😃➗😃😃'
>>> converter.convert(-1.12)
'-😃➗😁😃😃'
>>> converter.convert(.123)
'-😁➗😁😃😃😁😃😃'
```

  To get a list of functions in the module run `dir(converter)`, or `help(converter)`.

  To get help on respective functions run `help(converter.<function-name>)`.
