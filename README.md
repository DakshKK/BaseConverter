# **BaseConverter**

BaseConverter is a calculator written to convert numbers betwewen arbitrary bases 2 to 36. It takes a direct approach of converting the number without first shifting to decimal base.

This program was meant to reverse the process of converting ints from Bases 2 to 36 to decimal using the int function, and to provide the user with means to convert it from say base 5 to base 32, instead of only being able to convert to decimal base.

Hence the conversion of (102421)<sub>5</sub> to base 32 is successful as shown in the provided screenshot.

<ul>
  
![](output.png?raw=true)
</ul>

### TODO
  - [ ] Implement a system to let user enter their own system of digits, and accordinlgy convert inspired by [python-baseconv](https://github.com/semente/python-baseconv)
     ##### Issues
     - Base would be limited to 36, if operated using my direct algorithm
     - Base would be limited to user digit space if using the [baseconv.py](https://github.com/semente/python-baseconv/blob/master/baseconv.py) algorithm, of first converting to an int
  - [ ] Write a PyPi package for this repo, so users can utilise it more easily
  - [ ] Integrate a *TUI*, or implement my own, using **ANSI** sequences to provide a better interface with the package itself
