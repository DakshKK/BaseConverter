# BaseConverter

BaseConverter is a calculator written to convert numbers betwewen arbitrary bases from `2` to `36`. It takes a direct approach of converting the number without first shifting to decimal base.

This program was meant to reverse the process of converting ints from Bases `2` to `36` to decimal using the int function, and to provide the user with means to convert it from say base `5` to base `32`, instead of only being able to convert to decimal base.

Hence the conversion of `(102421)`<sub>`5`</sub> to base `32` is successful as shown in the provided screenshot.

<ul>

![](output.png?raw=true)
</ul>

### TODO
  - [x] Implement a system to let user enter their own system of digits, and accordinlgy convert inspired by [python-baseconv](https://github.com/semente/python-baseconv 'Base Converter, which uses decimal algorithm for conversion between bases.').
  - [ ] Write a PyPI package for this repo, so users can utilise it more easily, by doing a `pip install`.
  - [ ] Include working examples in a separate file, which imports the package, utilising, both direct, and decimal algorithm.
    - [x] Direct algorithm implementation complemeted.
    - [ ] Decimal algorithm implementation complemeted.

#### Info
  - User can now convert using their own digit space, but only till a maximum of base `36`. (Base is case-sensitive, hence `A` and `a` are not same).
  - Base is defined as length of your digit space. Hence `'abcd1234'`, is Base `8`.
  - **Repeated characters in base, or sign in digit-space, will lead to error**.

### EXAMPLES
  A working example is provided in the `example.py` script, which runs if the module name (**\_\_name__**) is **\_\_main__**.

### Install and Usage
  The repo can be directly cloned, and you can import the module in current directory.

  Example usage:

```python3
>>> # To use user defined bases
>>> import converter
>>> fro = {
... 'digit': '24',
... 'sign': '*',
... 'base': 2, # Length of digit
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
```

  To get a list of functions in the module run `dir(converter)`, or `help(converter)`.

  To get help on respective functions run `help(converter.<function-name>)`.
